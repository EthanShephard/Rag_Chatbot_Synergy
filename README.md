# RAG Chatbot

## Overview

The RAG Chatbot is an AI-powered question-answering system designed to provide accurate, context-aware responses using an organization's internal knowledge base.

Unlike traditional Large Language Models that rely solely on pre-trained knowledge, this system retrieves relevant information from indexed company documents before generating a response. This Retrieval-Augmented Generation (RAG) approach significantly improves factual accuracy while reducing hallucinations.

The chatbot is intended for enterprise deployment and can be integrated with internal documentation repositories, product catalogs, technical manuals, standard operating procedures, and other proprietary knowledge sources.

---

# Objectives

- Deliver accurate responses grounded in company documentation
- Minimize hallucinations by restricting answers to retrieved context
- Support conversational interactions through session-based memory
- Provide low-latency streaming responses
- Enable scalable document retrieval using vector search
- Maintain a modular and extensible backend architecture

---

# Key Features

## Intelligent Retrieval

- Semantic vector search
- BM25 keyword search
- Hybrid retrieval
- Reciprocal Rank Fusion (RRF)
- Context ranking
- Top-K retrieval

## Response Generation

- Context-aware prompting
- Streaming response generation
- Markdown support
- Reduced hallucinations
- Local LLM inference

## Backend Services

- FastAPI REST API
- Session management
- Conversation memory
- Modular retrieval pipeline
- Scalable architecture

---

# System Architecture

```text
                        User Query
                             │
                             ▼
                  Sentence Transformer
                             │
                    Query Embedding
                             │
        ┌────────────────────┴────────────────────┐
        │                                         │
        ▼                                         ▼
 Semantic Search (Qdrant)               BM25 Keyword Search
        │                                         │
        └────────────────────┬────────────────────┘
                             ▼
               Reciprocal Rank Fusion (RRF)
                             │
                             ▼
                 Top Ranked Knowledge Chunks
                             │
                             ▼
                  Prompt Construction Layer
                             │
                             ▼
                      Ollama Language Model
                             │
                             ▼
                   Streaming Response Engine
                             │
                             ▼
                          Frontend
```

---

# Retrieval Pipeline

The chatbot processes each request through the following stages:

## 1. Query Processing

The user's question is received through the REST API.

---

## 2. Embedding Generation

The query is converted into a dense vector representation using a Sentence Transformer model.

---

## 3. Hybrid Retrieval

Two retrieval strategies are executed simultaneously.

### Semantic Search

Uses dense vector similarity within Qdrant to retrieve conceptually relevant document chunks.

### Keyword Search

Uses BM25 to identify documents containing exact terminology, product names, model numbers, and technical keywords.

---

## 4. Reciprocal Rank Fusion

Results from semantic search and BM25 are merged using Reciprocal Rank Fusion (RRF), improving both precision and recall.

---

## 5. Prompt Construction

The highest-ranked document chunks are combined with conversation history and system instructions to form the final prompt.

---

## 6. Response Generation

The constructed prompt is sent to the language model running through Ollama.

Responses are streamed incrementally to the client for improved responsiveness.

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Backend | FastAPI |
| Programming Language | Python |
| Vector Database | Qdrant Cloud |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Language Model | Ollama |
| Retrieval | Hybrid (Semantic + BM25) |
| Ranking | Reciprocal Rank Fusion |
| Frontend | HTML, CSS, JavaScript |
| Memory Storage | JSON Session Storage |

---

# Directory Structure

```text
project/
│
├── app.py
├── chatbot.py
├── retrieval.py
├── memory.py
├── requirements.txt
│
├── data/
│   ├── chunks.json
│   └── metadata.json
│
├── embeddings/
│   └── chunk_embeddings.npy
│
├── memory/
│   └── sessions/
│
├── frontend/
│   ├── index.html
│   ├── css/
│   └── js/
│
└── static/
```

---

# Components

## FastAPI Backend

Responsible for:

- Request handling
- Session management
- Streaming responses
- API endpoints
- Communication with the retrieval pipeline

---

## Retrieval Engine

Responsible for:

- Query embedding
- Semantic retrieval
- BM25 retrieval
- Hybrid ranking
- Context selection

---

## Vector Database

Qdrant stores:

- Dense embeddings
- Chunk identifiers
- Metadata
- Payload information

Approximate Nearest Neighbor (ANN) search enables efficient retrieval over large document collections.

---

## Embedding Model

**BAAI/bge-small-en-v1.5**

Used for generating dense vector representations of user queries.

---

## Language Model

The chatbot utilizes Ollama for local inference.

Responsibilities include:

- Answer generation
- Context interpretation
- Conversational reasoning
- Streaming token generation

---

# Session Memory

Each conversation is assigned a unique session identifier.

Session memory stores:

- User messages
- Assistant responses
- Conversation history
- Session summaries

This enables coherent multi-turn conversations while controlling prompt size.

---

# Streaming Responses

Responses are streamed token-by-token instead of waiting for complete generation.

Benefits include:

- Reduced perceived latency
- Improved user experience
- Progressive markdown rendering
- Real-time response visualization


---


# Retrieval Workflow

```text
User Question
      │
      ▼
Generate Embedding
      │
      ▼
Semantic Search
      │
      ▼
BM25 Search
      │
      ▼
Hybrid Ranking
      │
      ▼
Retrieve Top Context
      │
      ▼
Prompt Construction
      │
      ▼
Language Model
      │
      ▼
Streaming Response
```

---

# Current Capabilities

- Hybrid document retrieval
- Semantic search
- Keyword search
- Session-aware conversations
- Streaming response generation
- Markdown rendering
- Modular backend architecture
- Scalable vector database integration
- Local language model inference

---

# Planned Enhancements

- Document upload interface
- Automated document ingestion
- OCR support for scanned PDFs
- Citation and source attribution
- Web search fallback
- User authentication
- Role-based access control
- Administrative dashboard
- Analytics and usage monitoring
- Cloud deployment
- Docker containerization
- Multi-tenant support

---

# License

This software is intended for internal organizational use. Distribution and usage are subject to company policies and applicable licensing agreements.