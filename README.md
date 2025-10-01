# Rouh Perfume Shop Chatbot E-Commerce Platform

**Rouh** is a modern, full-stack e-commerce application specializing in premium perfumes, integrated with a powerful AI chatbot named **Aria**. Aria acts as a personalized perfume consultant, providing real-time recommendations and customer support using **Retrieval-Augmented Generation (RAG)**, user context, and current weather data.

## ✨ Key Features

* **AI Perfume Consultant (Aria):** A Gemini 1.5 Flash-powered chatbot that uses RAG to provide personalized fragrance recommendations based on product data, user preferences, and real-time context.
* **Context-Aware Recommendations:** Aria considers the user's current **location and weather** conditions, along with keywords extracted from their message, to tailor its advice.
* **Fast & Scalable Retrieval:** Implements RAG using a **FAISS Vector Store** and Sentence Transformers (`all-MiniLM-L6-v2`) for efficient similarity search across the perfume catalog.
* **Full-Stack Architecture:** Built with a Python FastAPI backend and a React/Vite frontend for a modular and high-performance system.
* **User Interaction Logging:** All user-chatbot interactions (messages, replies, location, and weather data) are logged to **MongoDB** for quality assurance and future model training.

---

## 🛠️ Tech Stack

### Backend & AI
* **Python:** Core programming language.
* **FastAPI:** High-performance web framework for the API.
* **Gemini API:** Powers the `PerfumeAgent` (Aria) for natural language understanding and generation.
* **RAG/Vector DB:** **FAISS** index, built with **Sentence Transformers** for efficient semantic search of product data.
* **Database:** **MongoDB** for persisting user interaction and session history.
* **Utilities:** `python-dotenv`, `requests`, `geocoder`, `yake` (for keyword extraction).

### Frontend (React/Vite)
* **React:** Frontend library for the user interface.
* **JSX/CSS:** Component and styling structure, including dedicated files like `ChatWidget.css`.

---

## 📂 Project Structure (Backend/AI Focus)

The Python backend is organized for separation of concerns and maintainability.

```
.
├── src/
│   ├── controllers/
│   │   └── ObjectUserDataCont.py           # Pydantic Schemas for API payloads
│   ├── database/
│   │   └── mongo_handler.py              # MongoDB handler for data persistence
│   ├── LLMFactory/
│   │   ├── ChatBotmodel.py               # Factory pattern for different LLMs (Gemini, Llama)
│   │   ├── KeywordExtractorContFactory.py  # Factory for keyword extractors (YAKE)
│   │   └── PerfumeAgent.py               # The main agent logic and decision maker (Aria)
│   ├── modules/
│   │   └── WeatherLoc.py                 # External API calls for location/weather data
│   ├── RAGSystem/
│   │   └── RetrievalModel/
│   │       └── PerfumeRetrieval.py       # FAISS/Sentence-Transformer RAG implementation
│   ├── data/
│   │   └── data.json                     # Product catalog (implied from other files)
│   ├── main.py                           # FastAPI entry point and API routes
├── docker-compose.yaml                   # MongoDB setup
└── README.md
```


---

## 🚀 Getting Started

### Prerequisites

1.  **Python 3.x** and **Node.js/npm** (for the frontend).
2.  **API Keys:** **GEMINI\_API\_KEY** and **WEATHER\_API\_KEY\_2**.
3.  **Docker:** To run the MongoDB instance.

### 1. Setting up Environment Variables

Create a **`.env`** file in the appropriate location and populate it with your API keys:

```dotenv
# .env file content
GEMENI_API_KEY="YOUR_GEMINI_API_KEY"
WEATHER_API_KEY_2="YOUR_OPENWEATHERMAP_API_KEY"
# Optional: MongoDB URI if not using Docker default
MONGO_URI="mongodb://localhost:27027"
```


2. Building the Vector Database (RAG Index)
Your RAG system requires a pre-built FAISS index (perfume.index) and its corresponding metadata file (metadata.json) located in src/data/perfume_faiss/. These files are typically created by running the embedding process outlined conceptually in the RAG_VC_DB.ipynb notebook.

3. Running the Services
A. Start MongoDB with Docker
Use the provided docker-compose.yaml to run MongoDB on port 27027 (mapped from the internal 27017):


```Bash

docker-compose up -d
```

B. Start the FastAPI Backend
Navigate to the source directory, install dependencies, and run the FastAPI application:

```Bash

# Assuming you are in the project root
cd src
pip install -r requirements.txt # Use your project's dependency file
uvicorn main:app --reload --port 8000
The API will be available at http://127.0.0.1:8000.
```

C. Start the React Frontend
Navigate to your frontend project directory (e.g., my-app), install dependencies, and start the development server:

```Bash

# Assuming you are in the frontend directory (e.g., my-app)
npm install
npm run dev # or npm start
```

💡 Chatbot Interaction Flow
When a user sends a message to Aria:

The POST /user_response endpoint is triggered.

The PerfumeRetrievalFAISS performs a semantic search against the product vector database, retrieving the top relevant products.

The system retrieves the user's location and current weather data.

The PerfumeAgent generates a response, leveraging the retrieved products as context, along with the weather data and its expert persona (Aria).

The entire interaction (message, reply, location, weather) is saved to MongoDB.

The final reply, along with extracted keywords and context data, is returned to the frontend.

