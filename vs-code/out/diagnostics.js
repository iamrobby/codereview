"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.showReviewReport = showReviewReport;
const vscode = require("vscode");
let outputChannel;
function showReviewReport(issues) {
    if (!outputChannel) {
        outputChannel = vscode.window.createOutputChannel("AI Code Review");
    }
    outputChannel.clear();
    outputChannel.show(true);
    if (!issues || issues.length === 0) {
        outputChannel.appendLine("✅ No issues found.");
        return;
    }
    outputChannel.appendLine("🔍 AI Code Review Report\n");
    issues.forEach((issue, index) => {
        outputChannel.appendLine(`Issue ${index + 1}`);
        outputChannel.appendLine(`Type      : ${issue.issue_type}`);
        outputChannel.appendLine(`Severity  : ${issue.severity}`);
        outputChannel.appendLine(`Line      : ${issue.line_number}`);
        outputChannel.appendLine(`Problem   : ${issue.explanation}`);
        outputChannel.appendLine(`Fix       : ${issue.suggested_fix}`);
        outputChannel.appendLine("—".repeat(40));
    });
}
//# sourceMappingURL=diagnostics.js.map