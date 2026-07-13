const UI = (() => {
    const chatBox =
        document.getElementById("chat-box");
    const input =
        document.getElementById("message-input");
    const sendBtn =
        document.getElementById("send-btn");
    const suggestions =
        document.getElementById("suggestions");
    const hero =
        document.getElementById("hero");
    const registrationCard =
        document.getElementById("registration-card");
    const toast =
        document.getElementById("toast");
    const typingQueues = new WeakMap();
    function escapeHTML(text) {
        const div =
            document.createElement("div");
        div.textContent = text;
        return div.innerHTML;
    }
    function currentTime() {
        return new Date().toLocaleTimeString(
            [],
            {
                hour: "2-digit",
                minute: "2-digit"
            }
        );
    }
    function timestampHTML() {
        return `
            <div class="timestamp">
                ${currentTime()}
            </div>
        `;
    }
    function scrollBottom() {
        requestAnimationFrame(() => {
            chatBox.scrollTo({
                top:
                    chatBox.scrollHeight,
                behavior:
                    "smooth"
            });
        });
    }
    function autoResize() {
        input.style.height = "auto";
        input.style.height =
            input.scrollHeight + "px";
    }
    function setLoading(state) {
        sendBtn.disabled = state;
        sendBtn.classList.toggle(
            "loading",
            state
        );
    }
    function renderMarkdown(
        element,
        markdown
    ) {
        element.innerHTML =
            marked.parse(markdown);
        element
            .querySelectorAll("pre code")
            .forEach(block => {
                hljs.highlightElement(block);
            });
        element
            .querySelectorAll("a")
            .forEach(link => {
                link.target =
                    "_blank";
                link.rel =
                    "noopener noreferrer";
            });
    }
    function showToast(message) {
        if (!toast)
            return;
        toast.textContent =
            message;
        toast.classList.add("show");
        clearTimeout(
            toast.timer
        );
        toast.timer =
            setTimeout(() => {
                toast.classList.remove(
                    "show"
                );
            }, 1800);
    }
    function hideSuggestions() {
        if (!suggestions)
            return;
        suggestions.style.display =
            "none";
    }
    function showSuggestions() {
        if (!suggestions)
            return;
        suggestions.style.display =
            "flex";
    }
    function hideHero() {
        if (!hero)
            return;
        hero.classList.add("hide");
    }
    function showHero() {
        if (!hero)
            return;
        hero.classList.remove("hide");
    }
    function addUserMessage(text) {
        hideHero();
        hideSuggestions();
        const wrapper =
            document.createElement("div");
        wrapper.className =
            "message-wrapper user-wrapper";
        wrapper.innerHTML = `
            <div class="message user">
                <div class="user-content">
                    ${escapeHTML(text)}
                </div>
                ${timestampHTML()}
            </div>
        `;
        chatBox.appendChild(wrapper);
        scrollBottom();
    }
    function createBotMessage() {
        const wrapper =
            document.createElement("div");
        wrapper.className =
            "message-wrapper bot-wrapper";
        wrapper.innerHTML = `
            <div class="message bot">
                <div
                    class="bot-content streaming"
                ></div>
                ${timestampHTML()}
                <div class="message-actions">
                    <button
                        class="copy-btn"
                        title="Copy"
                    >
                        📋
                    </button>
                    <button
                        class="like-btn"
                        title="Helpful"
                    >
                        👍
                    </button>
                    <button
                        class="dislike-btn"
                        title="Not Helpful"
                    >
                        👎
                    </button>
                </div>
            </div>
        `;
        chatBox.appendChild(wrapper);
        scrollBottom();
        return wrapper;
    }
    function appendChunk(wrapper, chunk) {
        const content = wrapper.querySelector(".bot-content");

        if (!typingQueues.has(content)) {
            typingQueues.set(content, {
                buffer: "",
                displayed: "",
                typing: false
            });
        }

        const state = typingQueues.get(content);

        state.buffer += chunk;

        if (!state.typing) {
            state.typing = true;
            typeWriter(content, state);
        }
    }
    function typeWriter(content, state) {

        let speed = 1;
        let delay = 40;

        if (state.buffer.length > 500) {
            speed = 4;
            delay = 10;
        }
        else if (state.buffer.length > 250) {
            speed = 3;
            delay = 20;
        }
        else if (state.buffer.length > 100) {
            speed = 2;
            delay = 30;
        }

        if (state.buffer.length === 0) {
            state.typing = false;
            return;
        }

        state.displayed += state.buffer.slice(0, speed);
        state.buffer = state.buffer.slice(speed);

        renderMarkdown(content, state.displayed);
        scrollBottom();

        setTimeout(() => {
            typeWriter(content, state);
        }, delay);
    }
    function finishMessage(wrapper) {
        const content =
            wrapper.querySelector(".bot-content");
        const state =
            typingQueues.get(content);
        if (state) {
            // Flush everything still waiting
            state.displayed += state.buffer;
            state.buffer = "";
            renderMarkdown(
                content,
                state.displayed
            );
            typingQueues.delete(content);
        }
        content.classList.remove("streaming");
        scrollBottom();
    }
    function showTyping() {
        removeTyping();
        const wrapper =
            document.createElement("div");
        wrapper.id =
            "typing-indicator";
        wrapper.className =
            "message-wrapper bot-wrapper";
        wrapper.innerHTML = `
            <div class="message bot">
                <div class="typing">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        `;
        chatBox.appendChild(wrapper);
        scrollBottom();
    }
    function removeTyping() {
        document
            .getElementById(
                "typing-indicator"
            )
            ?.remove();
    }
    function createRegistrationCard(onSubmit) {
        removeRegistrationCard();
        const wrapper = document.createElement("div");
        wrapper.id = "registration-card";
        wrapper.className =
            "message-wrapper bot-wrapper";
        wrapper.innerHTML = `
            <div class="message bot registration-card">
                <h2>Welcome 👋</h2>
                <p>
                    Before we continue,
                    please register to use Synapse AI.
                </p>
                <input
                    id="customer-name"
                    type="text"
                    placeholder="Full Name"
                >
                <input
                    id="customer-email"
                    type="email"
                    placeholder="Email Address"
                >
                <input
                    id="customer-company"
                    type="text"
                    placeholder="Company"
                >
                <input
                    id="customer-phone"
                    type="tel"
                    placeholder="Phone Number"
                >
                <button id="register-btn">
                    Continue →
                </button>
            </div>
        `;
        chatBox.appendChild(wrapper);
        wrapper
            .querySelector("#register-btn")
            .addEventListener(
                "click",
                () => {
                    onSubmit({
                        name: wrapper.querySelector("#customer-name").value.trim(),
                        email: wrapper.querySelector("#customer-email").value.trim(),
                        company: wrapper.querySelector("#customer-company").value.trim(),
                        phone: wrapper.querySelector("#customer-phone").value.trim()
                    });
                }
            );
        scrollBottom();
    }
    function removeRegistrationCard() {
        document
            .getElementById(
                "registration-card"
            )
            ?.remove();
    }
    async function copyMessage(button) {
        const content =
            button
                .closest(".message")
                .querySelector(".bot-content");
        if (!content)
            return;
        try {
            await navigator.clipboard.writeText(
                content.innerText
            );
            showToast(
                "Copied to clipboard"
            );
        }
        catch {
            showToast(
                "Unable to copy"
            );
        }
    }
    function react(
        button,
        emoji
    ) {
        button
            .parentElement
            .querySelectorAll("button")
            .forEach(btn => {
                btn.classList.remove(
                    "active"
                );
            });
        button.classList.add(
            "active"
        );
        showToast(
            `${emoji} Feedback received`
        );
    }
    function clearChat() {
        chatBox.innerHTML = "";
        removeRegistrationCard();
        showHero();
        showSuggestions();
        scrollBottom();
    }
    function showQuickReplies(question, replies) {
        const wrapper = createBotMessage();
        const bubble = wrapper.querySelector(".message.bot");
        const content = wrapper.querySelector(".bot-content");

        // this isn't a streamed response, so don't leave the blinking
        // cursor sitting under the question forever
        content.classList.remove("streaming");
        content.innerHTML = `<p>${question}</p>`;

        if (!Array.isArray(replies) || replies.length === 0) {
            scrollBottom();
            return;
        }

        const container = document.createElement("div");
        container.className = "quick-replies";

        replies.forEach(reply => {
            const button = document.createElement("button");

            // Backend now sends {text, value} pairs so the button can show
            // friendly display text while sending the real option value
            // back to survey_engine.py (which matches on option["value"]).
            // Falling back to treating `reply` itself as both is just a
            // safety net for older/plain-string quickReplies payloads.
            const label = (reply && typeof reply === "object") ? reply.text : reply;
            const value = (reply && typeof reply === "object") ? reply.value : reply;

            button.className = "quick-reply";
            button.textContent = label;

            button.onclick = () => {
                addUserMessage(label);
                container.remove();
                Chat.sendQuickReply(value);
            };

            container.appendChild(button);
        });

        // append inside the message bubble itself, not the outer
        // flex wrapper — otherwise it renders as a sibling next to
        // the bubble instead of underneath the question text
        bubble.appendChild(container);

        scrollBottom();
    }
    function showQuantityStepper(question, opts = {}) {
        const wrapper = createBotMessage();
        const bubble = wrapper.querySelector(".message.bot");
        const content = wrapper.querySelector(".bot-content");

        content.classList.remove("streaming");
        renderMarkdown(content, question);

        const min = opts.min ?? 1;
        const max = opts.max ?? 9999;
        let value = opts.default ?? min;

        const container = document.createElement("div");
        container.className = "quantity-stepper";
        container.innerHTML = `
            <button class="qty-btn qty-minus" type="button" aria-label="Decrease quantity">−</button>
            <span class="qty-value">${value}</span>
            <button class="qty-btn qty-plus" type="button" aria-label="Increase quantity">+</button>
            <button class="qty-confirm" type="button">Confirm</button>
        `;

        const valueEl = container.querySelector(".qty-value");
        const minusBtn = container.querySelector(".qty-minus");
        const plusBtn = container.querySelector(".qty-plus");
        const confirmBtn = container.querySelector(".qty-confirm");

        function render() {
            valueEl.textContent = value;
            minusBtn.disabled = value <= min;
            plusBtn.disabled = value >= max;
        }

        minusBtn.onclick = () => {
            value = Math.max(min, value - 1);
            render();
        };

        plusBtn.onclick = () => {
            value = Math.min(max, value + 1);
            render();
        };

        confirmBtn.onclick = () => {
            addUserMessage(String(value));
            container.remove();
            Chat.sendQuickReply(String(value));
        };

        render();

        // same reasoning as showQuickReplies — append inside the
        // bubble itself so the stepper sits under the question text
        bubble.appendChild(container);

        scrollBottom();
    }
    function showSurveyComplete(message, actions) {
        const wrapper = createBotMessage();
        const bubble = wrapper.querySelector(".message.bot");
        const content = wrapper.querySelector(".bot-content");

        content.classList.remove("streaming");
        renderMarkdown(content, message);

        if (!Array.isArray(actions) || actions.length === 0) {
            scrollBottom();
            return;
        }

        const container = document.createElement("div");
        container.className = "quick-replies";

        actions.forEach(action => {
            const button = document.createElement("button");

            button.className = "quick-reply";
            button.textContent = action.label;

            button.onclick = () => {
                if (action.url) {
                    window.open(
                        action.url,
                        "_blank",
                        "noopener,noreferrer"
                    );
                    return;
                }
                if (action.mailto) {
                    const subject =
                        encodeURIComponent(action.subject || "");
                    const body =
                        encodeURIComponent(action.body || "");
                    window.location.href =
                        `mailto:${action.mailto}?subject=${subject}&body=${body}`;
                }
            };

            container.appendChild(button);
        });

        // same reasoning as showQuickReplies — append inside the
        // bubble itself so the buttons sit under the drafted email
        bubble.appendChild(container);

        scrollBottom();
    }
    function waitForRegistration(){
        return new Promise(resolve=>{
            createRegistrationCard(resolve);
        });
    }
    return {
        chatBox,
        input,
        sendBtn,
        suggestions,
        escapeHTML,
        currentTime,
        timestampHTML,
        scrollBottom,
        autoResize,
        setLoading,
        renderMarkdown,
        showToast,
        hideHero,
        showHero,
        hideSuggestions,
        showSuggestions,
        addUserMessage,
        createBotMessage,
        appendChunk,
        finishMessage,
        showTyping,
        removeTyping,
        createRegistrationCard,
        removeRegistrationCard,
        waitForRegistration,
        showQuickReplies,
        showQuantityStepper,
        showSurveyComplete,
        copyMessage,
        react,
        clearChat
    };
})();