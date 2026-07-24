const placeholders = [
    "Ask about RF Connectors...",
    "Search Product Catalogues...",
    "Tell me about Cable Assemblies...",
    "Find Microwave Components...",
    "Ask Synergy AI anything..."
];

let placeholderIndex = 0;

// Fallback for browsers without 100dvh support: mobile browsers report
// 100vh as the height *before* the keyboard/address bar changes the
// visible area, which pushes the composer off-screen. We recalculate
// the real visible height into a CSS var on load/resize so .app can
// use calc(var(--vh, 1vh) * 100) as a middle-ground fallback between
// the plain 100vh and 100dvh rules in style.css.
function setViewportHeightVar() {
    const vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty("--vh", `${vh}px`);
}

window.addEventListener("resize", setViewportHeightVar);
window.addEventListener("orientationchange", setViewportHeightVar);
if (window.visualViewport) {
    window.visualViewport.addEventListener("resize", setViewportHeightVar);
}

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

    setViewportHeightVar();

    Events.init();

    UI.input.focus();

    UI.autoResize();

    rotatePlaceholder();

    setInterval(
        rotatePlaceholder,
        3500
    );

    console.log(
        "%cSynergy AI Ready",
        "color:#60a5fa;font-size:18px;font-weight:bold;"
    );

}

window.addEventListener(
    "DOMContentLoaded",
    initialize
);
