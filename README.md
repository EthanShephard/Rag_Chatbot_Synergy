# Synergy AI — RAG Chatbot

An AI-powered product information and customer-assistance chatbot built for **Synergy Telecom**.

Synergy AI uses Retrieval-Augmented Generation (RAG) to answer questions using indexed company and product data rather than relying only on a language model's pretrained knowledge.

The system combines local semantic retrieval, BM25 keyword search, conversation-aware query scoping, persistent session memory, customer registration, an interactive product-finder survey, and streamed LLM responses through the DeepSeek API.

---

## Overview

Synergy AI is designed as a customer-facing knowledge assistant for Synergy Telecom.

Users can ask questions about products, specifications, product categories, pricing information, catalogues, and related technical information.

Instead of sending a user's question directly to an LLM, the application first searches an indexed knowledge base for relevant information. Retrieved content is then supplied to the language model as grounded context for generating the final response.

The application currently includes:

* Retrieval-Augmented Generation
* Local semantic vector search
* BM25 keyword retrieval
* Hybrid retrieval using Reciprocal Rank Fusion
* Conversation-aware keyword-scoped retrieval
* Streaming AI responses
* Persistent session memory
* Automatic conversation summarization
* Customer registration
* Pending-question recovery after registration
* Interactive product-finder survey
* Lead capture
* AI-generated sales enquiry drafts
* Responsive browser-based chat interface

---

# Architecture

```text
                         User
                           │
                           ▼
                    Web Frontend
                HTML / CSS / JavaScript
                           │
                           ▼
                     FastAPI API
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
       Registration   Survey Engine   RAG Chat
             │             │             │
             │             │             ▼
             │             │      Conversation Memory
             │             │             │
             │             │             ▼
             │             │      Query + History Scope
             │             │             │
             │             │             ▼
             │             │      Retrieval Engine
             │             │        ┌────┴────┐
             │             │        │         │
             │             │        ▼         ▼
             │             │     BM25      Semantic
             │             │     Search      Search
             │             │        │         │
             │             │        └────┬────┘
             │             │             ▼
             │             │      Ranked Context
             │             │             │
             │             │             ▼
             │             │      Prompt Construction
             │             │             │
             │             │             ▼
             │             └──────► DeepSeek API
             │                           │
             └───────────────────────────┤
                                         ▼
                                Streaming Response
                                         │
                                         ▼
                                     Frontend
```

---

# Core Features

## 1. Retrieval-Augmented Generation

Synergy AI grounds responses in an indexed product and company knowledge base.

The RAG pipeline:

1. Receives the user's question.
2. Loads recent conversation context.
3. Extracts useful keywords and technical specifications.
4. Narrows the searchable document scope when possible.
5. Ranks relevant chunks using BM25 and/or semantic retrieval.
6. Builds a grounded prompt from the retrieved chunks.
7. Sends the prompt to DeepSeek.
8. Streams the generated response back to the frontend.

The system prompt explicitly instructs the model not to invent unsupported product specifications, pricing, certifications, compatibility claims, or URLs.

---

## 2. Local Semantic Search

Semantic retrieval uses:

```text
BAAI/bge-large-en-v1.5
```

Document embeddings are precomputed and stored locally as NumPy arrays.

```text
chunks.json
        │
        ▼
BAAI/bge-large-en-v1.5
        │
        ▼
Normalized Embeddings
        │
        ├── chunk_embeddings.npy
        └── chunk_ids.npy
```

At query time, the user's question is embedded using the same Sentence Transformer model.

Because both query and document embeddings are L2-normalized, cosine similarity can be calculated efficiently using a matrix dot product:

```text
scores = chunk_embeddings @ query_embedding
```

This avoids requiring an external vector database for the current dataset.

---

## 3. BM25 Keyword Search

The application uses `rank-bm25` for lexical retrieval.

BM25 is particularly useful for queries containing:

* Product names
* Model numbers
* Connector types
* Technical terminology
* Frequency specifications
* Impedance values
* Exact catalogue terminology

The BM25 index is cached using Joblib to avoid rebuilding it unnecessarily on every application startup.

The cache is automatically considered stale when `chunks.json` has been modified.

---

## 4. Hybrid Retrieval

The retrieval engine supports both:

```text
Semantic Search
      +
BM25 Keyword Search
      │
      ▼
Reciprocal Rank Fusion
      │
      ▼
Ranked Knowledge Chunks
```

Semantic search captures conceptual similarity, while BM25 performs well for exact terminology.

The `hybrid_search()` pipeline combines both result sets using **Reciprocal Rank Fusion (RRF)**.

Globally unique chunk IDs are used during result fusion to prevent unrelated chunks from being incorrectly merged.

---

## 5. Conversation-Aware Keyword-Scoped Retrieval

The primary conversational retrieval path uses a cascading keyword-scoping strategy.

For follow-up questions such as:

```text
User: Show me RF cables.

Assistant: ...

User: What are the prices?
```

the second question alone contains very little retrieval context.

Synergy AI therefore combines:

* The current question
* Recent user messages
* The previous assistant response

to preserve conversational scope.

Technical expressions such as:

```text
50 ohm
6 GHz
12 mm
```

are extracted as high-value search terms.

Keywords are progressively applied to narrow the candidate document set before BM25 ranking.

If a keyword would over-restrict retrieval, the system can retain the broader candidate set instead.

This improves multi-turn product discovery without requiring an additional LLM query-rewriting call.

---

# Retrieval Pipeline

```text
User Question
      │
      ▼
Load Conversation History
      │
      ▼
Extract Keywords + Technical Terms
      │
      ▼
Add Recent Conversation Context
      │
      ▼
Cascading Keyword Scope
      │
      ▼
BM25 Ranking
      │
      ├──────────── fallback / hybrid path ────────────┐
      │                                                │
      │                                   ┌────────────┴────────────┐
      │                                   │                         │
      │                                   ▼                         ▼
      │                            Semantic Search              BM25 Search
      │                                   │                         │
      │                                   └────────────┬────────────┘
      │                                                ▼
      │                                      Reciprocal Rank Fusion
      │                                                │
      └───────────────────────────────┬────────────────┘
                                      ▼
                             Top Knowledge Chunks
                                      │
                                      ▼
                              Context Sanitization
                                      │
                                      ▼
                              Prompt Construction
                                      │
                                      ▼
                                 DeepSeek API
                                      │
                                      ▼
                              Streaming Response
```

---

# Context Sanitization

Retrieved data is sanitized before being passed to the language model.

The retrieval layer includes safeguards for sensitive or potentially misleading catalogue data.

### Email filtering

Email addresses found in scraped content are removed unless they match the approved official contact email.

This prevents personal, partner, or unrelated email addresses from accidentally appearing in customer responses.

### Pricing metadata filtering

Internal pricing disclaimers and sourcing metadata are removed before generation.

The model receives only the information necessary to distinguish verified pricing from estimated pricing.

### Structured price conversion

Certain known catalogue row formats containing bare USD values can be converted into estimated INR values programmatically before reaching the LLM.

This keeps deterministic data transformations in application code rather than relying on the language model to perform inconsistent calculations.

---

# Language Model

The application uses the **DeepSeek API** through its OpenAI-compatible interface.

Current model:

```text
deepseek-v4-flash
```

The model is used for:

* Grounded answer generation
* Conversation-aware responses
* Streaming completion
* Conversation summarization
* Product enquiry / sales email drafting

The API key is loaded through:

```text
DEEPSEEK_API_KEY
```

The application disables extended thinking for the main RAG response path so responses can begin streaming directly.

---

# Prompt Grounding

The system includes a detailed prompt specifically designed for Synergy Telecom.

The prompt enforces several important rules:

* Retrieved content is the source of truth for product facts.
* Product specifications must not be invented.
* Pricing must not be fabricated.
* Different products must not have their specifications incorrectly merged.
* URLs must correspond to the product or claim being discussed.
* Internal sourcing information must not be exposed.
* Responses should remain concise and customer-facing.
* Synergy AI speaks as an official Synergy Telecom assistant.

This provides an additional grounding layer on top of retrieval.

---

# Streaming Responses

LLM responses are streamed incrementally from the backend.

```text
DeepSeek
    │
    ▼
Streaming Completion
    │
    ▼
FastAPI StreamingResponse
    │
    ▼
Fetch ReadableStream
    │
    ▼
Incremental Markdown Rendering
```

The frontend progressively renders incoming content using Markdown.

This reduces perceived latency because users begin seeing the answer before the full generation is complete.

The frontend also includes:

* Markdown rendering
* Syntax highlighting
* Typewriter-style streaming
* Automatic scrolling
* Copy controls
* Feedback controls
* Typing indicators
* Request timeout handling

---

# Session Memory

Each user receives a unique session ID.

The frontend stores the session identifier in:

```text
localStorage
```

The backend stores session state as JSON files under:

```text
backend/memory/sessions/
```

A session contains:

```text
messages
summary
survey state
```

Conversation history is used to maintain context across multiple turns.

---

## Conversation Summarization

The application limits the amount of raw conversation history retained in the active prompt.

The configured history limit is:

```text
16 messages
```

Older conversation content can be summarized before history is pruned.

This allows the chatbot to retain longer-term conversational context without continuously increasing prompt size.

Per-session file locking is used to reduce the risk of concurrent requests overwriting the same session state on a single server instance.

---

# Customer Registration

Before normal chatbot access, users are required to register.

Registration collects:

```text
Name
Email
Company
Phone Number
```

Customer records are stored per session.

The backend validates:

* Required name
* Required company
* Email format
* Phone-number format

---

## Pending Question Recovery

If an unregistered user asks a question:

```text
User asks question
        │
        ▼
Registration required
        │
        ▼
Original question saved
        │
        ▼
User completes registration
        │
        ▼
Original question restored
        │
        ▼
RAG pipeline executes automatically
        │
        ▼
Answer streamed to user
```

This prevents users from having to re-enter their original question after registration.

---

# Product Finder Survey

The application includes an interactive product-finder survey.

Users can start it with:

```text
start survey
```

or through the frontend's product-finder interface.

The survey guides users through product categories such as:

* RF Connectors
* Cable Assemblies
* Microwave Components
* Antennas
* Waveguides
* RF Adaptors
* Filters
* Installation Tools & Kits
* Test & Measurement
* Masts

Depending on the selected category, the survey asks for:

```text
Product Category
      │
      ▼
Product / Subcategory
      │
      ▼
Quantity
      │
      ▼
Email
      │
      ▼
Lead Generation
```

The frontend supports quick-reply buttons and a quantity stepper for this flow.

---

# Lead Capture and Sales Enquiries

Completed survey responses can be stored as lead data.

Lead information is written to:

```text
backend/database/leads.jsonl
```

File locking is used when writing lead records.

The application can also generate a structured sales enquiry using the language model and expose actions for:

* Contacting sales
* Opening a relevant product page

Product pricing fields are intentionally designed to support real per-unit pricing when verified price data becomes available.

---

# Frontend

The frontend is implemented using vanilla:

```text
HTML
CSS
JavaScript
```

No frontend framework is required.

The interface includes:

* Responsive chat UI
* Product suggestion chips
* Streaming assistant responses
* Markdown rendering
* Syntax highlighting
* Customer registration form
* Survey quick replies
* Quantity selector
* Product enquiry actions
* Copy controls
* Feedback controls
* Keyboard shortcuts
* Rotating prompt suggestions

The frontend uses browser `fetch()` and `ReadableStream` APIs to consume streamed responses.

---

# API

The FastAPI backend exposes the primary application endpoints.

## Health Check

```http
GET /
```

Returns application status information.

Example:

```json
{
  "status": "running",
  "message": "Synergy Chatbot API"
}
```

---

## Chat

```http
POST /chat
```

Example request:

```json
{
  "message": "Show me 50 ohm RF cables",
  "session_id": "optional-existing-session-id"
}
```

If no session ID is supplied, the backend generates one.

Depending on application state, the endpoint may return:

* A streaming chatbot response
* A registration-required response
* A survey question
* A completed survey result

The session ID is also returned through:

```text
X-Session-ID
```

---

## Registration

```http
POST /register
```

Example:

```json
{
  "session_id": "session-id",
  "name": "Customer Name",
  "email": "customer@example.com",
  "company": "Example Company",
  "phone": "+91XXXXXXXXXX"
}
```

After successful registration, any pending question associated with the session can automatically continue through the chatbot pipeline.

---

# Project Structure

```text
Rag_Chatbot_Synergy/
│
├── backend/
│   │
│   ├── app.py
│   ├── chatbot.py
│   ├── config.py
│   ├── customer.py
│   ├── memory.py
│   ├── prompt.py
│   ├── retrieval.py
│   ├── summarizer.py
│   ├── survey.py
│   ├── survey_engine.py
│   │
│   ├── database/
│   │   ├── chunks.json
│   │   ├── chunk_embeddings.npy
│   │   ├── chunk_ids.npy
│   │   ├── bm25_cache.joblib
│   │   ├── embedchunks.py
│   │   └── leads.jsonl          # generated when leads are stored
│   │
│   └── memory/
│       └── sessions/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── logo.jpg
│   │
│   └── js/
│       ├── api.js
│       ├── chat.js
│       ├── events.js
│       ├── main.js
│       └── ui.js
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Backend Components

## `app.py`

Main FastAPI application.

Responsible for:

* Application initialization
* Retrieval warm-up
* CORS configuration
* Session ID generation
* `/chat` endpoint
* `/register` endpoint
* Registration enforcement
* Survey routing
* Streaming responses
* Serving the frontend under `/app`

---

## `chatbot.py`

Main RAG orchestration layer.

Responsible for:

* Loading conversation history
* Loading conversation summaries
* Conversation-aware retrieval
* Building retrieved context
* Sanitizing context
* Prompt construction
* DeepSeek API communication
* Streaming generation
* Saving conversation turns
* Triggering conversation summarization

---

## `retrieval.py`

Search and retrieval engine.

Responsible for:

* Loading `chunks.json`
* Loading precomputed embeddings
* Loading the Sentence Transformer
* BM25 index construction
* BM25 cache management
* Semantic similarity search
* Hybrid search
* Reciprocal Rank Fusion
* Keyword extraction
* Technical-spec extraction
* Cascading keyword filtering
* Conversation-aware retrieval scope
* Pricing-data sanitization
* Email sanitization

---

## `memory.py`

Persistent conversation state management.

Responsible for:

* Session creation
* Loading sessions
* Saving sessions
* Conversation history
* Conversation summaries
* Survey state
* Per-session file locking

---

## `summarizer.py`

Handles long-conversation compression.

When conversation history exceeds the configured threshold, older messages can be summarized and stored in the session summary while newer messages remain available as raw conversation history.

---

## `customer.py`

Customer registration and persistence layer.

Responsible for:

* Customer records
* Registration validation
* Registration status
* Pending-question storage
* Pending-question restoration
* Per-customer file locking

---

## `prompt.py`

Contains the primary Synergy AI system prompt.

Defines:

* Assistant identity
* Grounding rules
* Product-answer behavior
* Pricing behavior
* Contact-information policy
* URL handling
* Conversational style
* Hallucination restrictions

---

## `survey.py`

Defines the product-finder survey structure.

Contains:

* Survey nodes
* Product categories
* Subcategories
* Quantity input configuration
* Email collection
* Product URLs
* Pricing placeholders

Business logic is kept separate from the survey definition.

---

## `survey_engine.py`

Executes the product-finder workflow.

Responsible for:

* Starting surveys
* Processing answers
* Input validation
* Navigating survey nodes
* Recording lead information
* Generating enquiry content
* Returning product and email actions

---

# Knowledge Base

The core retrieval dataset is stored in:

```text
backend/database/chunks.json
```

Each chunk contains indexed text and associated metadata.

The system relies on a globally unique:

```text
id
```

for each chunk.

This ID is used to map:

```text
Embedding
    ↕
Chunk ID
    ↕
Original Knowledge Chunk
```

Using globally unique IDs is important because document-local `chunk_id` values may repeat across different source documents.

---

# Embedding Generation

Embeddings can be regenerated using the embedding script in the database package.

The script:

1. Loads `chunks.json`.
2. Validates that chunk IDs are globally unique.
3. Loads `BAAI/bge-large-en-v1.5`.
4. Encodes every chunk.
5. L2-normalizes embeddings.
6. Saves the embedding matrix.
7. Saves the corresponding chunk-ID array.

Generated files:

```text
chunk_embeddings.npy
chunk_ids.npy
```

The retrieval engine and embedding-generation script must use the same embedding model.

> Note: the current embedding script explicitly targets CUDA. Adjust the SentenceTransformer device configuration if embeddings need to be generated on a CPU-only system.

---

# Technology Stack

| Component              | Technology                                  |
| ---------------------- | ------------------------------------------- |
| Backend                | FastAPI                                     |
| Backend Language       | Python                                      |
| LLM API                | DeepSeek                                    |
| LLM Interface          | OpenAI-compatible SDK                       |
| Main LLM               | `deepseek-v4-flash`                         |
| Embedding Model        | `BAAI/bge-large-en-v1.5`                    |
| Semantic Retrieval     | Local NumPy cosine similarity               |
| Keyword Retrieval      | BM25                                        |
| Hybrid Ranking         | Reciprocal Rank Fusion                      |
| Embedding Storage      | NumPy `.npy` files                          |
| BM25 Cache             | Joblib                                      |
| Session Storage        | JSON files                                  |
| Concurrency Protection | FileLock                                    |
| Frontend               | HTML, CSS, JavaScript                       |
| Markdown Rendering     | Marked                                      |
| Code Highlighting      | Highlight.js                                |
| API Framework          | FastAPI                                     |
| Streaming              | FastAPI `StreamingResponse` + Fetch Streams |

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd Rag_Chatbot_Synergy
```

---

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

The project uses packages including:

```text
fastapi
uvicorn
sentence-transformers
torch
numpy
rank-bm25
python-dotenv
pydantic
requests
beautifulsoup4
openai
langchain-text-splitters
```

The current source also imports `filelock` and `joblib`, so ensure they are installed in the deployment environment:

```bash
pip install filelock joblib
```

---

# Environment Configuration

Create a `.env` file in the project root:

```env
DEEPSEEK_API_KEY=your_deepseek_api_key
```

Do not commit API keys or secrets to version control.

---

# Running the Application

Start FastAPI from the project root:

```bash
uvicorn backend.app:app --host 0.0.0.0 --port 8000
```

For local development with automatic reload:

```bash
uvicorn backend.app:app --reload
```

The API health endpoint is available at:

```text
/
```

The frontend is served by FastAPI at:

```text
/app/
```

The frontend can therefore use the backend through the same origin when deployed together.

---

# Retrieval Startup

At application startup, FastAPI initializes the retrieval system.

The startup process:

```text
FastAPI Startup
      │
      ▼
Load chunks.json / BM25 cache
      │
      ▼
Build BM25 if required
      │
      ▼
Load BGE Embedding Model
      │
      ▼
Load chunk_embeddings.npy
      │
      ▼
Load chunk_ids.npy
      │
      ▼
Retrieval Ready
```

If precomputed embeddings are unavailable, semantic retrieval can be disabled and the system can fall back to BM25-based retrieval.

---

# Regenerating Embeddings

When `chunks.json` changes, embeddings should be regenerated so the vector representation matches the current knowledge base.

The embedding script is located at:

```text
backend/database/embedchunks.py
```

Run the appropriate module/script from the project root after updating the knowledge base.

The generated files must remain synchronized:

```text
chunks.json
chunk_embeddings.npy
chunk_ids.npy
```

The BM25 cache is separately invalidated when `chunks.json` is newer than the cached index.

---

# Current Capabilities

* Retrieval-Augmented Generation
* Local semantic search
* BM25 lexical retrieval
* Reciprocal Rank Fusion
* Conversation-aware keyword-scoped search
* Technical specification extraction
* Persistent conversation memory
* Conversation summarization
* DeepSeek streaming generation
* Customer registration
* Registration validation
* Pending-question recovery
* Product-finder survey
* Lead capture
* AI-generated enquiry drafts
* Markdown rendering
* Syntax highlighting
* Responsive frontend
* Same-origin frontend/backend deployment
* Retrieval cache optimization
* Per-session file locking
* Context sanitization

---

# Current Storage Model

The application currently uses filesystem-based persistence for several components:

```text
Session memory      → JSON files
Customer records    → JSON files
Lead records        → JSONL
Knowledge chunks    → JSON
Embeddings          → NumPy arrays
BM25 index cache    → Joblib
```

This architecture is simple and effective for a single application instance.

For horizontal scaling across multiple servers, these components should eventually move to shared infrastructure such as:

* PostgreSQL
* Redis
* Object storage
* Centralized vector/search infrastructure where appropriate

Local `FileLock` synchronization only protects concurrent access on the same machine.

---

# Production Considerations

Before larger-scale production deployment, consider adding:

* Persistent database-backed customer storage
* Redis or database-backed session management
* Authentication and authorization
* Rate limiting
* Structured logging
* Centralized error monitoring
* Automated tests
* CI/CD
* Docker containerization
* Secret management
* Restricted production CORS configuration
* HTTPS termination
* Analytics and observability
* Automated knowledge-base ingestion
* Retrieval evaluation
* Response quality monitoring

---

# Future Improvements

Potential future development includes:

* Automated website synchronization
* Automated PDF ingestion
* OCR for scanned documents
* Incremental embedding updates
* Source citations in generated answers
* Administrative dashboard
* Knowledge-base management interface
* User authentication
* Role-based access control
* CRM integration
* Sales lead management
* Usage analytics
* Retrieval quality evaluation
* Reranking models
* Multi-tenant knowledge bases
* Automated deployment pipelines
* Database-backed session persistence

---

# Design Philosophy

Synergy AI separates the major application concerns into independent layers:

```text
Frontend
    │
API Layer
    │
Application / Conversation Logic
    │
Retrieval
    │
Knowledge Base
    │
LLM Generation
```

This makes individual components easier to replace or extend.

For example:

* The LLM provider can be changed without redesigning retrieval.
* Local vector search can later be replaced with a vector database.
* JSON session storage can be replaced with Redis or PostgreSQL.
* The static knowledge base can be connected to an automated ingestion pipeline.
* The vanilla JavaScript frontend can be replaced without rewriting the RAG backend.

The result is a modular RAG architecture that can evolve from a single-instance product assistant into a larger production knowledge platform.

---

# License

This project is intended for internal organizational and development use.

Distribution, deployment, and use of company data are subject to Synergy Telecom policies and any applicable third-party software, model, API, and data licensing terms.
