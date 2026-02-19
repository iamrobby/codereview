# AI Code Review VS Code Extension(V-0.0.1)

AI Code review is a Visual Studio Code extension that provides AI- agent powered code reviews directly within your editor. It helps you identify bugs, security vulnerabilities, performance issues, and style inconsistencies in your code.

## Architecture

The project is composed of two main parts:

1.  **Python Backend (`/backend`)**: A FastAPI server that handles the core logic. It receives code from the VS Code extension, uses the ScaleDown API to compress it, and then sends it to the Google Gemini LLM for analysis. The review results are returned as a structured JSON response.
2.  **VS Code Extension (`/vs-code`)**: A TypeScript-based extension that integrates with the VS Code UI. It allows users to trigger a code review on the current file or a specific selection, communicates with the Python backend, and displays the results in the VS Code Output Channel.

## Features

-   **On-Demand Analysis**: Run a review on an entire file or just a selected block of code.
-   **Comprehensive Feedback**: Get insights on bugs, security flaws, performance bottlenecks, and code style.
-   **Direct Integration**: View the review report directly in the VS Code "AI Code Review" output panel without leaving your editor.
-   **Detailed Issues**: Each issue includes a type, severity level, line number, explanation, and a suggested fix.

## Setup and Installation

### Prerequisites

-   [Node.js](https://nodejs.org/) and npm
-   [Python 3.8+](https://www.python.org/) and pip
-   [Visual Studio Code](https://code.visualstudio.com/)

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the `backend` directory and add your API keys:
    ```env
    GEMINI_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"
    SCALEDOWN_API_KEY="YOUR_SCALEDOWN_API_KEY"
    ```

5.  **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```
    The server will be running at `http://localhost:8000`.

### VS Code Extension Setup

1.  **Navigate to the extension directory:**
    ```bash
    cd vs-code
    ```

2.  **Install Node.js dependencies:**
    ```bash
    npm install
    ```

3.  **Compile the TypeScript code:**
    ```bash
    npm run compile
    ```

4.  **Run the Extension:**
    -   Open the `vs-code` directory in Visual Studio Code.
    -   Press `F5` to open a new Extension Development Host window. This new window will have the AI Code Review extension running.

## How to Use

1.  Ensure the backend server is running.
2.  In the VS Code Extension Development Host window, open any code file.
3.  To review the entire file, simply open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
4.  To review a specific part of the code, select the desired lines before opening the Command Palette.
5.  In the Command Palette, type `Run AI Code Review` and press `Enter`.
6.  A notification will appear indicating the review is in progress.
7.  Once complete, the **Output** panel will automatically open and display the "AI Code Review" report with any identified issues.

## Technology Stack

-   **Backend**: Python, FastAPI, Uvicorn
-   **AI & Services**: Google Gemini, ScaleDown API
-   **VS Code Extension**: TypeScript, VS Code API
