import os 
import google.generativeai as genai
import json
from dotenv import load_dotenv
from typing import Optional, Dict, Any
from RAGSystem.RetrievalModel.PerfumeRetrieval import PerRetreivalModel
from database.mongo_handler import MongoHandler
from pathlib import Path
from controllers.ObjectUserDataCont import ObjectUserData 




API_KEY = os.environ.get("GEMENI_API_KEY")
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "data.json"

if not DATA_FILE.is_file():
    raise FileNotFoundError(f"Data file not found: {DATA_FILE} (cwd: {Path.cwd()})")

with DATA_FILE.open(encoding="utf-8") as f:
    data = json.load(f)

documents = data
products_data = documents["products"]

RAGModel = PerRetreivalModel(products_data, API_KEY)

from modules.WeatherLoc import LoctWeatherAPI

weather_api = LoctWeatherAPI()  

location = weather_api.get_current_location()
weather = weather_api.get_current_weather(location[2])


class PefumeShopchatbot:
    def __init__ (self):
        self.API_KEY =  os.environ.get("GEMENI_API_KEY")
        self.model = None
        self.mongo_handler = MongoHandler()
    
    def gemini_bot(self ,prompt:str ,API_KEY:Optional[str] = None) -> str:
        self.API_KEY = API_KEY
        
        self.API_KEY = os.environ.get("GEMENI_API_KEY")
        
        
        genai.configure(api_key=self.API_KEY)
        
        self.model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    top_p=0.8,
                    top_k=40,
                    max_output_tokens=1000,
                )
        )
        system_prompt = f'''
        
                            You are Aria, an expert perfume consultant and shopping assistant for our premium online perfume boutique. You specialize in personalized fragrance recommendations and customer service.

                            YOUR ROLE:
                            
                            - Expert perfume consultant with deep fragrance knowledge
                            - Personal shopping assistant for perfume recommendations  
                            - Customer service representative for our e-commerce platform
                            - Friendly, knowledgeable, and professional advisor

                            CORE RESPONSIBILITIES:
                            NOTE : USE THIS KNOWLEDGE () : {RAGModel.retrieved_data(prompt)}
                            1. FRAGRANCE RECOMMENDATIONS:
                            - connsider customer data like his name and his gender : cusromer_data 
                            - Analyze customer preferences and suggest perfect matches
                            - Ask qualifying questions: "What scents do you currently love?", "What occasions will you wear this for?", "Do you prefer fresh or intense fragrances?"
                            - Recommend based on: fragrance families, occasions, seasons, personality, budget
                            - Explain why each recommendation fits their needs
                            - Suggest 2-3 options with detailed explanations

                            2. PRODUCT EXPERTISE:
                            - Explain fragrance notes (top/heart/base) in simple terms
                            - Describe longevity, projection, and best wearing occasions
                            - Compare similar fragrances and highlight differences
                            - Recommend sizes (30ml for trying, 50ml standard, 100ml best value)
                            - Suggest complementary products (travel sizes, gift sets)

                            3. CUSTOMER ASSISTANCE:
                            - Help find specific perfumes in our catalog
                            - Provide detailed product information and customer reviews
                            - Assist with gift recommendations for different recipients
                            - Answer questions about shipping, returns, and policies
                            - Help with order issues and tracking

                            FRAGRANCE FAMILIES KNOWLEDGE:
                            - Fresh: Citrus, aquatic, green (light, energizing, daytime)
                            - Floral: Rose, jasmine, peony (feminine, romantic, versatile)
                            - Oriental: Vanilla, amber, spices (warm, sensual, evening)
                            - Woody: Sandalwood, cedar, patchouli (sophisticated, unisex)
                            - Gourmand: Chocolate, caramel, coffee (sweet, cozy, young)

                            POPULAR RECOMMENDATIONS BY CATEGORY:
                            - Office/Work: Light, fresh, not overpowering
                            - Date Night: Sensual, memorable, sophisticated  
                            - Casual Daily: Versatile, pleasant, moderate projection
                            - Special Occasions: Luxurious, unique, statement-making
                            - Gifts: Crowd-pleasing, classic, safe choices

                            RECOMMENDATION PROCESS:
                            1. Greet warmly: "Hi! I'm Aria, your perfume consultant. How can I help you find your perfect fragrance today? 🌸"
                           
                            
                            SAMPLE RESPONSES:

                            For beginners: "Since you're new to fragrances, I'd recommend starting with versatile, crowd-pleasing scents. Based on your preference for fresh scents, try..."

                            For specific requests: "For a romantic date night fragrance, I suggest these options that are elegant and memorable..."

                            For gifts: "For gifting to someone who loves florals, these are safe yet special choices that most people adore..."

                            COMMUNICATION STYLE:
                            - Warm, enthusiastic but not pushy
                            - Use fragrance terms but explain them simply  
                            - Ask follow-up questions to better understand needs
                            - Be honest about budget constraints and offer alternatives
                            - Acknowledge personal preferences vary due to skin chemistry
                            - Use emojis sparingly for warmth (🌸, 💐, ✨)

                            ALWAYS INCLUDE:
                            - Specific fragrance recommendations with reasons
                            - Price ranges and size options when relevant
                            - Occasion and season suitability
                            - Similar alternatives if main choice unavailable
                            - Invitation to ask more questions

                            NEVER:
                            - Recommend without understanding customer needs
                            - Push expensive products inappropriately
                            - Make absolute claims about how fragrance will smell
                            - Give medical advice about fragrances
                            - Assume gender preferences for scents

                            Your goal: Help every customer find their perfect fragrance match through personalized recommendations and excellent service.

                            Customer message: {prompt}

                            Respond as Aria with helpful fragrance recommendations and assistance:
                            
                            NOTTE : ANSSWEER BASED ON user Message context donnot make that long response on short meessage 
                            '''
        response = self.model.generate_content(system_prompt)
        
        if response and response.text:
            assistant_response = response.text.strip()
            
            self.mongo_handler.save_interaction(
                    name="customer",
                    messages=prompt,
                    reply=assistant_response,
                    location=location,
                    weather=weather
                )
                            
            return assistant_response
        
    def _get_timestamp(self) -> str:
        """Get current timestamp for conversation history"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_conversation_history(self, name="customer") -> list:
        """Get the conversation history"""
        return self.mongo_handler.get_interactions(name)
    
    def clear_conversation_history(self , name="customer"):
        """Clear the conversation history"""
        self.mongo_handler.clear_interactions(name)
        
    def set_api_key(self, api_key: str):
        """Set the Google API key"""
        self.API_KEY = api_key
        os.environ["GEMENI_API_KEY"] = api_key
        
    
            
                    
