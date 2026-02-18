"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
const vscode = require("vscode");
const api_1 = require("./api");
const diagnostics_1 = require("./diagnostics");
function activate(context) {
    const command = vscode.commands.registerCommand("aiCodeReview.run", async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showWarningMessage("No active editor");
            return;
        }
        const code = editor.document.getText(editor.selection.isEmpty
            ? undefined
            : editor.selection);
        vscode.window.withProgress({
            location: vscode.ProgressLocation.Notification,
            title: "Running AI Code Review...",
            cancellable: false
        }, async () => {
            const result = await (0, api_1.sendForReview)(code, editor.document.languageId);
            (0, diagnostics_1.showReviewReport)(result.issues);
        });
    });
    context.subscriptions.push(command);
}
//# sourceMappingURL=extension.js.map