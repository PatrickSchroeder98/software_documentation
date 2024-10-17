// footer.js
document.addEventListener("DOMContentLoaded", function () {
    const footerText = "&copy; 2024, Patrick Schröder, Software Documentation v1.3.6. All rights reserved. All logos are trademarks of their respective owners and are used here for informational purposes only.";
    const footerElement = document.querySelector("footer p[data-i18n='copyright']");
    if (footerElement) {
        footerElement.innerHTML = footerText;
    }
});