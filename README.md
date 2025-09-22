DarkWeb Watcher: An AI-Powered Intelligence Assistant 🛡️

About The Project 🚀
DarkWeb Watcher is a conversational AI assistant designed to provide real-time intelligence on cybersecurity and dark web topics. The bot leverages a Retrieval-Augmented Generation (RAG) architecture, combining a private knowledge base with live web search capabilities to deliver accurate, context-aware answers to user queries.
This project serves as a comprehensive demonstration of building a sophisticated AI application from the ground up, integrating a web UI, a vector database for specialized knowledge, and live data retrieval from web APIs.

Key Features ✨
Conversational AI: Powered by Google's Gemini Pro for natural and insightful responses.
Live Web Intelligence: Integrates with the Google Search API to retrieve up-to-the-minute information.
Specialized Knowledge Base: Uses a ChromaDB vector database to learn from private documents (e.g., security reports, threat briefs).
Interactive UI: Built with Streamlit, featuring a polished chat interface with real-time streaming responses.

Tech Stack ⚙️
Backend: Python
Frontend: Streamlit
AI & Language Model: Google Gemini API
Live Data Retrieval: Google Custom Search API
Vector Database: ChromaDB
Text Embedding Model: Sentence-Transformers
Document Loading: PyPDF

Setup and Installation 💻
Follow these steps to set up and run the project locally.
1. Clone the Repository
   
Bash
git clone https://github.com/your-username/DarkWeb-Watch-Bot.git
cd DarkWeb-Watch-Bot

3. Create a Virtual Environment
Bash
python -m venv venv

# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate
3. Install Dependencies
   
Bash
pip install -r requirements.txt

5. Set Up API Keys
Create a .env file in the root directory and add your secret API keys. This file is listed in .gitignore and should not be committed to the repository.

Code snippet
GEMINI_API_KEY="your-gemini-api-key"
GOOGLE_API_KEY="your-google-api-key"
SEARCH_ENGINE_ID="your-search-engine-id"

Usage 📖
The application has two main parts: ingesting private documents and running the chatbot.
1. Ingest Documents (Optional)
To build the private knowledge base, add your PDF files to the documents/ folder and run the ingestion script once.

Bash
python ingest_docs.py
This will create a db_storage folder containing the vector database.

2. Run the Chatbot
Start the Streamlit application with the following command:

Bash
streamlit run final_app.py
Open the provided localhost URL in your browser to start interacting with the bot.

Disclaimer ⚠️
This project is for educational purposes only. The information provided by the chatbot is generated based on public web data and user-provided documents and should not be considered professional security advice. Always consult with a qualified cybersecurity professional for specific threats.
