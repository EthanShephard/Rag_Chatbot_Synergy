import json
from pathlib import Path
from filelock import FileLock

BASE_DIR = Path(__file__).resolve().parent
MEMORY_DIR = BASE_DIR / "memory"
SESSIONS_DIR = MEMORY_DIR / "sessions"
SESSIONS_DIR.mkdir(parents=True, exist_ok=True)

MAX_MESSAGES = 16  # 8 user + 8 assistant

# Sessions are plain JSON files on local disk. That's fine for a single
# instance, but without locking, two requests touching the same
# session_id concurrently (e.g. a double-click send, or two tabs) can
# interleave their read-modify-write cycles and one update silently
# clobbers the other. A per-session FileLock serializes access to a
# given session's file without blocking unrelated sessions. Note this
# only guards a single machine's disk — it does not make the storage
# safe across multiple hosts; that needs a real shared store (DB/Redis)
# if this is ever scaled horizontally.
def _session_path(session_id: str) -> Path:
    return SESSIONS_DIR / f"{session_id}.json"


def _session_lock(session_id: str) -> FileLock:
    return FileLock(str(SESSIONS_DIR / f"{session_id}.json.lock"))

def create_session(session_id: str):
    path = _session_path(session_id)

    with _session_lock(session_id):
        if path.exists():
            return
        session = {
            "messages": [],
            "summary": "",

            "survey": {
                "active": False,
                "current": None,
                "answers": {}
            }
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(session, f, indent=4, ensure_ascii=False)


def load_session(session_id: str):
    create_session(session_id)

    path = _session_path(session_id)

    with _session_lock(session_id):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)


def save_session(session_id: str, session: dict):
    path = _session_path(session_id)

    with _session_lock(session_id):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(session, f, indent=4, ensure_ascii=False)

def save_session_state(session_id, session):

    save_session(
        session_id=session_id,
        session=session
    )
    
def load_history(session_id: str):
    session = load_session(session_id)

    return session["messages"]


def load_summary(session_id: str):
    session = load_session(session_id)

    return session["summary"]

def save_turn(
    session_id: str,
    user_message: str,
    assistant_message: str
):
    session = load_session(session_id)

    session["messages"].append(
        {
            "role": "user",
            "content": user_message
        }
    )

    session["messages"].append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )

    # NOTE: no trim_history() call here anymore. This used to
    # unconditionally cap session["messages"] to MAX_MESSAGES on every
    # turn, which ran *before* summarize_if_needed() ever got a chance
    # to see a list longer than MAX_MESSAGES — so its own
    # `len(messages) <= MAX_MESSAGES: return` guard fired every time and
    # the conversation was silently truncated with no summary ever
    # generated. summarize_if_needed() (backend/summarizer.py, called
    # right after save_turn() in chatbot.ask()) is now the single place
    # responsible for pruning history once it crosses MAX_MESSAGES —
    # it folds the older turns into session["summary"] before trimming,
    # instead of just discarding them.

    save_session(session_id, session)

def trim_history(session: dict):
    """
    Hard-cap session["messages"] with no summarization. Kept as a
    utility (e.g. for a manual reset) but no longer called
    automatically from save_turn() — see the note there.
    """

    messages = session["messages"]

    if len(messages) <= MAX_MESSAGES:
        return

    session["messages"] = messages[-MAX_MESSAGES:]

def save_summary(
    session_id: str,
    summary: str
):

    session = load_session(session_id)

    session["summary"] = summary

    save_session(session_id, session)

# NOTE: summarize_if_needed() used to be duplicated here as well as in
# backend/summarizer.py. This copy was never imported anywhere (chatbot.py
# imports summarize_if_needed from backend.summarizer, not backend.memory)
# and was broken besides — its conversation-join was missing the
# `for m in old_messages` clause entirely, so calling it would have raised
# a NameError. Removed rather than fixed, since backend/summarizer.py
# already has the correct, actually-used implementation and there's no
# reason to maintain two copies of the same logic.