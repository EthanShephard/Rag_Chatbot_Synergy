const Chat = (() => {
    let isSending = false;
    let pendingMessage = "";

    async function streamMessage(message) {
        UI.showTyping();
        let botMessage = null;
        try {
            const result = await API.post(
                message,
                chunk => {
                    if (!botMessage) {
                        UI.removeTyping();
                        botMessage = UI.createBotMessage();
                    }
                    UI.appendChunk(
                        botMessage,
                        chunk
                    );
                }
            );
            UI.removeTyping();

            // JSON response (Survey / Registration) — api.js already
            // tags this with { type: "survey" | "registration", ... }
            if (result) {
                return result;
            }

            if (botMessage) {
                UI.finishMessage(botMessage);
            }

            return null;
        }
        catch (error) {
            UI.removeTyping();
            if (!botMessage) {
                botMessage = UI.createBotMessage();
            }
            UI.appendChunk(
                botMessage,
`# ⚠️ Connection Error
Synergy AI couldn't generate a response.
**Reason**
\`${error.message}\`
Please try again.`
            );
            UI.finishMessage(botMessage);
            throw error;
        }
    }

    async function processMessage(message) {
        const result = await streamMessage(message);

        if (!result)
            return;

        // -------------------------
        // Survey
        // -------------------------
        if (result.type === "survey") {
            if (result.input === "quantity") {
                UI.showQuantityStepper(result.question, {
                    min: result.min,
                    max: result.max,
                    default: result.default
                });
            } else {
                UI.showQuickReplies(
                    result.question,
                    result.quickReplies
                );
            }
            return;
        }

        // -------------------------
        // Survey complete (drafted email + email/website actions)
        // -------------------------
        if (result.type === "survey_complete") {
            UI.showSurveyComplete(
                result.message,
                result.actions
            );
            return;
        }

        // -------------------------
        // Registration
        // -------------------------
        if (result.type === "registration") {
            pendingMessage = message;
            const customer = await UI.waitForRegistration();
            await completeRegistration(customer);
            return;
        }
    }

    async function send(displayText) {
        if (isSending)
            return;
        const message = UI.input.value.trim();
        if (!message)
            return;
        isSending = true;
        UI.addUserMessage(displayText || message);
        UI.input.value = "";
        UI.autoResize();
        UI.setLoading(true);
        try {
            // processMessage() already handles the survey/registration/
            // streaming branches internally and doesn't return anything
            // useful here — no extra handling needed after this call.
            await processMessage(message);
        }
        catch (error) {
            console.error(error);
        }
        finally {
            UI.setLoading(false);
            UI.input.focus();
            isSending = false;
        }
    }

    async function sendQuickReply(message) {
        if (isSending)
            return;
        isSending = true;
        UI.setLoading(true);
        try {
            await processMessage(message);
        }
        catch (error) {
            console.error(error);
        }
        finally {
            UI.setLoading(false);
            isSending = false;
        }
    }

    async function completeRegistration(customer) {
        UI.showTyping();
        let botMessage = null;
        try {
            await API.register(
                customer,
                chunk => {
                    if (!botMessage) {
                        UI.removeTyping();
                        botMessage = UI.createBotMessage();
                    }
                    UI.appendChunk(
                        botMessage,
                        chunk
                    );
                }
            );
            if (botMessage) {
                UI.finishMessage(botMessage);
            }
            UI.removeRegistrationCard();
            UI.showToast("Registration successful.");
        }
        finally {
            UI.removeTyping();
        }
    }

    async function copy(button) {
        await UI.copyMessage(button);
    }

    function react(button, emoji) {
        UI.react(button, emoji);
    }

    function clear() {
        pendingMessage = "";
        UI.clearChat();
    }

    return {
        send,
        sendQuickReply,
        copy,
        react,
        clear
    };
})();
