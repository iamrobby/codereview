import * as vscode from "vscode";
import { sendForReview } from "./api";
import { showReviewReport } from "./diagnostics";

export function activate(context: vscode.ExtensionContext) {
  const command = vscode.commands.registerCommand(
    "aiCodeReview.run",
    async () => {
      const editor = vscode.window.activeTextEditor;
      if (!editor) {
        vscode.window.showWarningMessage("No active editor");
        return;
      }

      const code = editor.document.getText(
        editor.selection.isEmpty
          ? undefined
          : editor.selection
      );

      vscode.window.withProgress(
        {
          location: vscode.ProgressLocation.Notification,
          title: "Running AI Code Review...",
          cancellable: false
        },
        async () => {
          const result = await sendForReview(
            code,
            editor.document.languageId
          );

          showReviewReport(result.issues);
        }
      );
    }
  );

  context.subscriptions.push(command);
}
