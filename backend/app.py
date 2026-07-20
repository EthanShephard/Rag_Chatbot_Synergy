from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path
import uuid

from backend.chatbot import ask
from backend.retrieval import initialize_retrieval
from backend.customer import (
    is_registered,
    register_customer,
    save_pending_question,
    load_pending_question,
    clear_pending_question,
)
from backend.memory import (
    load_session,
    save_session
)

from backend.survey_engine import (
    survey_engine
)

app = FastAPI(
    title="Synergy Chatbot API",
    version="1.0.0"
)

@app.on_event("startup")
async def warm_up_retrieval():
    """
    Loads chunks.json, builds the BM25 index, loads the embedding model,
    and connects to Qdrant once at process startup. initialize_retrieval()
    is idempotent (it no-ops on later calls once `chunks` is set), so this
    just moves the one-time cost from "whoever sends the first chat
    message" to "server boot" — and makes a bad QDRANT_URL/QDRANT_API_KEY
    show up immediately in the startup logs rather than as a crash on the
    first real user message.
    """
    initialize_retrieval()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=["*"] combined with allow_credentials=True is an
    # invalid combination per the CORS spec — browsers reject/strip
    # credentials on wildcard-origin responses. The frontend never sends
    # credentialed requests (session id travels via the JSON body +
    # localStorage, not cookies — see api.js), so there's nothing to
    # actually enable here. If cookie/session-based auth is added later,
    # swap allow_origins to an explicit list of real frontend origins
    # instead of turning this back on with "*".
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    # Browsers only expose a small "safe list" of response headers to
    # frontend JS by default (X-Session-ID is not one of them). Without
    # this, response.headers.get("X-Session-ID") in the frontend will
    # come back null once the frontend is served from a different origin
    # than the backend (e.g. company VPS -> Render), even though it may
    # have appeared to work under same-origin/local testing.
    expose_headers=["X-Session-ID"],
)


class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None


class CustomerRegistration(BaseModel):
    session_id: str
    name: str
    email: str
    company: str
    phone: str


@app.get("/")
async def home():
    return {
        "status": "running",
        "message": "Synergy Chatbot API"
    }


@app.post("/register")
async def register(customer: CustomerRegistration):
    try:

        register_customer(
            session_id=customer.session_id,
            name=customer.name,
            email=customer.email,
            company=customer.company,
            phone=customer.phone
        )

        question = load_pending_question(
            customer.session_id
        )

        clear_pending_question(
            customer.session_id
        )

        if not question:
            return {
                "success": True,
                "message": "Customer registered successfully.",
                "session_id": customer.session_id
            }

        return StreamingResponse(
            ask(
                question=question,
                session_id=customer.session_id
            ),
            headers={
                "X-Session-ID": customer.session_id
            },
            media_type="text/plain"
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=(f"Internal server error:{e}")
        )


@app.post("/chat")
async def chat(request: ChatRequest):
    try:

        if not request.session_id:
            request.session_id = str(uuid.uuid4())
        session = load_session(request.session_id)

        if request.message.strip().lower() == "start survey":

            response = survey_engine.start(session)

            save_session(
                request.session_id,
                session
            )

            return JSONResponse(
                content=response,
                headers={
                    "X-Session-ID": request.session_id
                }
            )

        if survey_engine.is_active(session):

            response = survey_engine.handle(
                session,
                request.message
            )

            save_session(
                request.session_id,
                session
            )

            return JSONResponse(
                content=response,
                headers={
                    "X-Session-ID": request.session_id
                }
            )

        if not is_registered(request.session_id):

            save_pending_question(
                request.session_id,
                request.message
            )

            return JSONResponse(
                status_code=403,
                content={
                    "registration_required": True,
                    "session_id": request.session_id,
                    "message": "Customer registration is required before using the chatbot."
                },
                headers={
                    "X-Session-ID": request.session_id
                }
            )
        return StreamingResponse(
            ask(
                question=request.message,
                session_id=request.session_id
            ),
            headers={
                "X-Session-ID": request.session_id
            },
            media_type="text/plain"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# CHANGED: serve the frontend from FastAPI itself, mounted at /app, so
# frontend and backend are same-origin. This matters specifically for
# GitHub Codespaces: each forwarded port gets its OWN separate public URL
# (e.g. https://name-8000.app.github.dev), so a frontend served any other
# way would need to know the backend's exact forwarded URL to reach it.
# Same-origin sidesteps that entirely — frontend/js/api.js's existing
# `BASE_URL = ""` fallback for non-localhost hosts already assumes
# same-origin, so no frontend changes are needed, just this mount.
# Mounted at /app rather than "/" so it doesn't shadow the existing JSON
# health-check route above at the bare "/" path. html=True serves
# index.html automatically at /app/.
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/app", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
