from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
import uuid

from backend.chatbot import ask
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
            detail="Internal server error: "
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