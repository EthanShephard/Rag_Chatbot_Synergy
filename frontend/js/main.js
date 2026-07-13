const placeholders = [
    "Ask about RF Connectors...",
    "Search Product Catalogues...",
    "Tell me about Cable Assemblies...",
    "Find Microwave Components...",
    "Ask Synapse anything..."
];

let placeholderIndex = 0;

function rotatePlaceholder() {

    if (document.activeElement === UI.input)
        return;

    placeholderIndex =
        (placeholderIndex + 1) %
        placeholders.length;

    UI.input.placeholder =
        placeholders[placeholderIndex];

}

function initialize() {

    Events.init();

    UI.input.focus();

    UI.autoResize();

    rotatePlaceholder();

    setInterval(
        rotatePlaceholder,
        3500
    );

    console.log(
        "%cSynapse AI Ready",
        "color:#60a5fa;font-size:18px;font-weight:bold;"
    );

}

window.addEventListener(
    "DOMContentLoaded",
    initialize
);