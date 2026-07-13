const API = (() => {

    const BASE_URL =
        location.hostname === "localhost" ||
        location.hostname === "127.0.0.1"
            ? "http://127.0.0.1:8000"
            : "";

    const CHAT_URL = `${BASE_URL}/chat`;
    const REGISTER_URL = `${BASE_URL}/register`;

    const DEFAULT_TIMEOUT = 2000000;

    let sessionId =
        localStorage.getItem("session_id");

    function getSessionId() {
        return sessionId;
    }

    function setSessionId(id) {

        if (!id)
            return;

        sessionId = id;

        localStorage.setItem(
            "session_id",
            id
        );

    }

    async function streamResponse(response, onChunk) {

        const returnedSession =
            response.headers.get("X-Session-ID");

        if (returnedSession) {
            setSessionId(returnedSession);
        }

        const contentType =
            response.headers.get("content-type") || "";

        if (contentType.includes("application/json")) {

            const data = await response.json();

            if (data.session_id) {
                setSessionId(data.session_id);
            }

            // Survey finished — has no "question" key, so it must be
            // checked before the survey-in-progress branch below or it
            // silently falls through to the untagged "json" type that
            // chat.js has no handler for.
            if (data.type === "survey_complete") {
                return {
                    type: "survey_complete",
                    ...data
                };
            }

            // Registration flow
            if (data.registration_required) {
                return {
                    type: "registration",
                    ...data
                };
            }

            // Survey flow
            if (data.question) {
                return {
                    type: "survey",
                    ...data
                };
            }

            return {
                type: "json",
                ...data
            };

        }

        const reader =
            response.body.getReader();

        const decoder =
            new TextDecoder();

        while (true) {

            const { done, value } =
                await reader.read();

            if (done)
                break;

            const chunk =
                decoder.decode(
                    value,
                    {
                        stream: true
                    }
                );

            if (onChunk) {
                onChunk(chunk);
            }

        }

        return null;

    }

    async function post(message, onChunk) {

        const controller =
            new AbortController();

        const timeout =
            setTimeout(
                () => controller.abort(),
                DEFAULT_TIMEOUT
            );

        try {

            const response =
                await fetch(
                    CHAT_URL,
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            message,
                            session_id: sessionId
                        }),
                        signal: controller.signal
                    }
                );

            clearTimeout(timeout);

            if (!response.ok &&
                response.status !== 403) {

                throw new Error(
                    `HTTP ${response.status}`
                );

            }

            return await streamResponse(
                response,
                onChunk
            );

        }

        catch (error) {

            clearTimeout(timeout);

            if (
                error.name ===
                "AbortError"
            ) {

                throw new Error(
                    "Request timed out."
                );

            }

            throw error;

        }

    }

    async function register(customer, onChunk) {

        const controller =
            new AbortController();

        const timeout =
            setTimeout(
                () => controller.abort(),
                DEFAULT_TIMEOUT
            );

        try {

            const response =
                await fetch(
                    REGISTER_URL,
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            session_id: sessionId,
                            name: customer.name,
                            email: customer.email,
                            company: customer.company,
                            phone: customer.phone
                        }),
                        signal: controller.signal
                    }
                );

            clearTimeout(timeout);

            if (!response.ok) {

                const error =
                    await response.text();

                throw new Error(error);

            }

            return await streamResponse(
                response,
                onChunk
            );

        }

        catch (error) {

            clearTimeout(timeout);

            if (
                error.name ===
                "AbortError"
            ) {

                throw new Error(
                    "Request timed out."
                );

            }

            throw error;

        }

    }

    return {

        post,
        register,
        getSessionId,
        setSessionId

    };

})();