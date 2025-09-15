from modules.WeatherLoc import LoctWeatherAPI
from RAGSystem.RetrievalModel.PerfumeRetrieval import PerfumeRetrievalFAISS
from database.mongo_handler import MongoHandler
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = SRC_DIR / "data" / "perfume_faiss" / "perfume.index"
METADATA_PATH = SRC_DIR / "data" / "perfume_faiss" / "metadata.json"

class AgentTools:
    def __init__(self , prudct_data , api_key):
        self.weather_api = LoctWeatherAPI()  
        self.location = self.weather_api.get_current_location()
        self.weather = self.weather_api.get_current_weather(self.location[2])
        self.rag = PerfumeRetrievalFAISS(
            index_path=str(INDEX_PATH),
            metadata_path=str(METADATA_PATH)
        )
        self.mongo = MongoHandler()
        
    
    def rag_search(self , query):
        return self.rag.search(query)
    
    
    def get_weather(self):
        return self.weather

    def save_interaction(self, name, prompt, reply, meta=None):
        self.mongo.save_interaction(name=name,
            messages=prompt,
            reply=reply,
            location=meta.get("location") if meta else None,
            weather=meta.get("weather") if meta else None 
        )
    def get_history(self, name="customer"):
        return self.mongo.get_interactions(name)

    def clear_history(self, name="customer"):
        self.mongo.clear_interactions(name)
        
        