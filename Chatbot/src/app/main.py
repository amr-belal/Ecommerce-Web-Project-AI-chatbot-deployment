from fastapi import FastAPI
# from routers import chat_router
from controllers.ObjectUserDataCont import ObjectUserData , ChatResponse
from modules.WeatherLoc import LoctWeatherAPI
from database.mongo_handler import MongoHandler
from LLMFactory.KeywordExtractorContFactory import Factory_Extractor
# from LLMFactory.PerfumeLLM import PefumeShopchatbot
from LLMFactory.AgentTools import AgentTools
from LLMFactory.ChatBotmodel import Factory
# السطر الصحيح
from RAGSystem.RetrievalModel.PerfumeRetrieval import PerfumeRetrievalFAISS
from LLMFactory.PerfumeAgent import PerfumeAgent
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = SRC_DIR / "data" / "perfume_faiss" / "perfume.index"
METADATA_PATH = SRC_DIR / "data" / "perfume_faiss" / "metadata.json"
agent = PerfumeAgent(api_key = os.environ.get("GEMENI_API_KEY"))

app = FastAPI(title="ChatGPT API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # أو ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
mongo_handler = MongoHandler()

# bot = PefumeShopchatbot()

# get extraxtor factory (yake)
extractor = Factory_Extractor.create("yake")
# app.include_router(chat_router.router)

retriever  = PerfumeRetrievalFAISS(
            index_path=str(INDEX_PATH),
            metadata_path=str(METADATA_PATH)
        )

@app.get("/")
def health_chek():
    return {"status": "ok"}


# first endpoint for the user Data 
weather_api = LoctWeatherAPI()

@app.post("/user_response" ,  response_model=ChatResponse)
def upload_user_data(userdata:ObjectUserData):
    
    retrieved_products = retriever.search(userdata.message, top_k=3)
    
    context = "\n".join([
        f"{p['name']} ({p['price']}$) - {p['description']}"
        for p in retrieved_products
    ])
    reply = agent.chat(
        f"User asked: {userdata.message}\n"
        f"Relevant products:\n{context}"
    , name=userdata.name)
    
    # reply = bot.gemini_bot(userdata.message) # for Rag Bot
    # location = weather_api.get_current_location()
    
    
    location = weather_api.get_current_location()
    if not location or not location[2]:
            # fallback location if city is None
            location = [30.0444, 31.2357, "Cairo", "EG", "Cairo, Egypt"]
    
    
    try:
            weather = weather_api.get_current_weather(location[2])
            
    except Exception:
            weather = ["unavailable", None]

    mongo_handler.save_interaction(
        name  = userdata.name,
        messages = userdata.message,
        location = location,
        weather = weather,
        reply = reply,
        
    )
    
    
    return ChatResponse(
        reply=reply,
        location=location,
        weather=weather,
        keywords = extractor.yake_keywords(userdata.message),
        recommend_products=[]
    )


