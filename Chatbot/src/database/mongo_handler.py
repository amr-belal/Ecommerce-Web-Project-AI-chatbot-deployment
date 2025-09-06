from pymongo import MongoClient

from datetime import datetime


class MongoHandler:
    def  __init__(self , uri="mongodb://localhost:27027" , db_name="chatbot_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["user_interactions"]
        
    def save_interaction(self , name , messages,location , weather,reply):
        # remember to add keywords after we add the model keyword extractor
        doc = {
            "name": name,
            "message": messages,
            # "keywords": keyword,
            "location": location,
            "weather": weather,
            "reply": reply,
            "timestamp": datetime.utcnow()
        }
        self.collection.insert_one(doc)
        return doc
    
    