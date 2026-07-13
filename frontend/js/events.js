const Events = (() => {
    function bindInput() {
        UI.input.addEventListener(
            "input",
            UI.autoResize
        );
        UI.input.addEventListener(
            "keydown",
            event => {
                if (
                    event.key === "Enter" &&
                    !event.shiftKey
                ) {
                    event.preventDefault();
                    Chat.send();
                }
            }
        );
    }
    function bindSendButton() {
        UI.sendBtn.addEventListener(
            "click",
            Chat.send
        );
    }
    function bindSuggestions() {
        document
            .querySelectorAll(".suggestion-chip")
            .forEach(chip => {
                chip.addEventListener(
                    "click",
                    () => {
                        const prompt =
                            chip.dataset.prompt ||
                            chip.innerText;
                        const label =
                            chip.dataset.label ||
                            prompt;

                        UI.input.value = prompt;
                        UI.autoResize();
                        Chat.send(label);
                    }
                );
            });
    }
    function bindChatActions() {
        UI.chatBox.addEventListener(
            "click",
            event => {
                const copy =
                    event.target.closest(
                        ".copy-btn"
                    );
                if (copy) {
                    Chat.copy(copy);
                    return;
                }
                const like =
                    event.target.closest(
                        ".like-btn"
                    );
                if (like) {
                    Chat.react(
                        like,
                        "👍"
                    );
                    return;
                }
                const dislike =
                    event.target.closest(
                        ".dislike-btn"
                    );
                if (dislike) {
                    Chat.react(
                        dislike,
                        "👎"
                    );
                }
            }
        );
    }
    function bindShortcuts() {
        document.addEventListener(
            "keydown",
            event => {
                if (
                    event.ctrlKey &&
                    event.key === "/"
                ) {
                    event.preventDefault();
                    UI.input.focus();
                }
                if (
                    event.ctrlKey &&
                    event.key.toLowerCase() === "l"
                ) {
                    event.preventDefault();
                    Chat.clear();
                }
            }
        );
    }
    function bindWindow() {
        window.addEventListener(
            "resize",
            UI.scrollBottom
        );
    }
    function init() {
        bindInput();
        bindSendButton();
        bindSuggestions();
        bindChatActions();
        bindShortcuts();
        bindWindow();
    }
    return {
        init
    };
})();