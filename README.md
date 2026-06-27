# 🤖 Stateful Chatbot with Summary Memory
This repository contains a Stateful Chatbot web application built using LangChain 🦜🔗 and Streamlit 💻.

Unlike traditional chatbots that pass the entire chat history to the LLM on every turn—which quickly exhausts token limits—this project implements an intelligent Conversation Summary Memory 🧠 strategy. It maintains a running summary of the conversation behind the scenes, allowing the bot to retain long-term context while keeping API requests lightweight and cost-efficient.

## ✨ Features
- 🚀 Interactive Web UI: A smooth, conversational interface powered by Streamlit's native chat components.
- 🧠 Smart Context Management: Uses LangChain to dynamically update a concise running summary of the conversation history.
- 🧩 Modular Architecture: Clean separation of concerns between backend LLM management, memory processing, and frontend display.
- 🛠️ Seamless Module Paths: Includes a root-level launcher script to eliminate Python path configuration issues.

## Project Structure
```
📁 langchain-project/
│
├── 📄 run_app.py          # 🚀 Root launcher script to run the Streamlit app
├── 📄 requirements.txt    # 📦 Project dependencies
├── 📄 .env                # 🔑 Environment variables (API keys - Git ignored)
└── 📁 src/
    ├── 📄 app.py          # 💻 Streamlit frontend UI logic
    └── 📄 summary_manager.py # 🧠 LangChain backend & summary chain logic
```

## Setup Instructions
Follow these steps to set up and run the project locally.
1. Clone the Repository
2. Set Up a Virtual Environment: Create and activate a virtual environment to manage dependencies cleanly.
```
# On macOS/Linux
python3 -m venv .venv
source .venv/bin/branch/activate

# On Windows
python -m venv .venv
.venv\Scripts\activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Configure Environment Variables: Create a .env file in the root directory of the project and add your OpenAI API key or Groq API key.
```
OPENAI_API_KEY=your_actual_api_key_here
GROQ_API_KEY=your_actual_api_key_here
```
5. Running the Application: To launch the web interface, run the main launcher script from the root directory.
```
python run_app.py
```

The application will automatically spin up a local server and open the chatbot interface in your default web browser!

Deployed application link: https://jcf6cvrxkesxywnz7kbar4.streamlit.app/
