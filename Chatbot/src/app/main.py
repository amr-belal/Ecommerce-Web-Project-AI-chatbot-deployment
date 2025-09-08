from fastapi import FastAPI
# from routers import chat_router
from controllers.ObjectUserDataCont import ObjectUserData , ChatResponse
from modules.WeatherLoc import LoctWeatherAPI
from database.mongo_handler import MongoHandler
from LLMFactory.KeywordExtractorContFactory import Factory_Extractor
from LLMFactory.PerfumeLLM import PefumeShopchatbot

from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="ChatGPT API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # أو ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
mongo_handler = MongoHandler()

bot = PefumeShopchatbot()

# get extraxtor factory (yake)
extractor = Factory_Extractor.create("yake")
# app.include_router(chat_router.router)


@app.get("/")
def health_chek():
    return {"status": "ok"}


# first endpoint for the user Data 
weather_api = LoctWeatherAPI()

@app.post("/user_response" ,  response_model=ChatResponse)
def upload_user_data(userdata:ObjectUserData):
    
    
    reply = bot.gemini_bot(userdata.message)
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

