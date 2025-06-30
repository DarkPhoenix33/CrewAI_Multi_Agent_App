# Multi-Agent PowerShell System

This project provides a Streamlit-based chatbot interface for interacting with a multi-agent system designed to automate and manage Windows environments using PowerShell. The system leverages CrewAI for agent orchestration and a custom PowerShell executor for command execution.

## Features

*   **Chatbot Interface:** Interact with the agents in a conversational manner.
*   **Session Memory:** Agents maintain context within the current chat session.
*   **Detailed Logs:** Toggle to view step-by-step execution logs, including tool calls and agent thoughts.
*   **Token Usage Tracking:** Monitor input and output token usage for each request.
*   **Persistent PowerShell Session:** Optimized PowerShell execution for faster command processing.

## Project Structure

*   `app.py`: The main Streamlit application file, containing the UI, agent definitions, and task orchestration.
*   `src/main.py`: (Originally contained agent definitions, now primarily for reference or future expansion if agents are moved back).
*   `src/tools/powershell_executor.py`: Custom CrewAI tool for executing PowerShell commands, featuring a persistent PowerShell session for efficiency.
*   `.env`: Environment file to store API keys (e.g., `OPENAI_API_KEY`).
*   `requirements.txt`: Lists all Python dependencies.

## Setup and Execution

Follow these steps to set up and run the project:

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd Gemini
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd D:\Gemini
    ```

3.  **Activate the virtual environment:**
    ```
    D:\Gemini\venv\Scripts\activate.bat
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up OpenAI API Key:**
    Create a file named `.env` in the root directory (`D:\Gemini\`) and add your OpenAI API key:
    ```
    OPENAI_API_KEY="your_openai_api_key_here"
    ```
    Replace `"your_openai_api_key_here"` with your actual OpenAI API key.

6.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

    This will open the Streamlit application in your web browser. If it doesn't open automatically, copy and paste the provided local URL (e.g., `http://localhost:8501`) into your browser.

## Usage

*   Type your commands or questions in the chat input field.
*   Use the "Clear Chat" button in the sidebar to reset the conversation.
*   Check the "Show detailed logs" checkbox to view the agent's step-by-step thought process and tool calls.
*   Monitor token usage in the sidebar.

