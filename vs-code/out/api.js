"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.sendForReview = sendForReview;
async function sendForReview(code, language) {
    const response = await fetch("http://localhost:8000/review", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code, language })
    });
    //log error
    if (!response.ok) {
        throw new Error(`Backend error: ${response.status}`);
    }
    return response.json();
}
//# sourceMappingURL=api.js.map