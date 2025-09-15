# from modules.WeatherLoc import LoctWeatherAPI

import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()

class GeminiModel:
    def __init__(self, model_name: str = "gemini-2.5-flash", api_key: str = None):
        self.model_name = model_name
        self.api_key = api_key or os.environ.get("GEMENI_API_KEY")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                top_p=0.8,
                top_k=40,
                max_output_tokens=1000,
            )
        )

    def generate_response(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text
    
class LLammaModel:
    pass 


class Factory:
    @staticmethod
    def get_model(model_type: str, **kwargs):
        if model_type == "gemini":
            return GeminiModel(**kwargs)
        elif model_type == "llama":
            return LLammaModel(**kwargs)
        else:
            raise ValueError(f"Unknown model type: {model_type}")

if __name__ == "__main__":
    # Example usage
    gemini = Factory.get_model("gemini")
    response = gemini.generate_response("Hello, how are you?")
    print(response)
# class Chatbot :
#     def __init__(self , model_name):
#         self.model_name = model_name
    
    
#     def gemeini_api(self , user_prompt , API_KEY = None):
#         self.API_KEY = os.environ.get("GOOGLE_API_KEY")

#         prompt = '''
#                 You are Aria, an expert perfume consultant and shopping assistant for our premium online perfume boutique. You specialize in personalized fragrance recommendations and customer service.

#                 YOUR ROLE:
#                 - Expert perfume consultant with deep fragrance knowledge
#                 - Personal shopping assistant for perfume recommendations
#                 - Customer service representative for our e-commerce platform
#                 - Friendly, knowledgeable, and professional advisor

#                 CORE RESPONSIBILITIES:

#                 1. FRAGRANCE RECOMMENDATIONS:
#                 - Analyze customer preferences and suggest perfect matches
#                 - Ask qualifying questions: "What scents do you currently love?", "What occasions will you wear this for?", "Do you prefer fresh or intense fragrances?"
#                 - Recommend based on: fragrance families, occasions, seasons, personality, budget
#                 - Explain why each recommendation fits their needs
#                 - Suggest 2-3 options with detailed explanations

#                 2. PRODUCT EXPERTISE:
#                 - Explain fragrance notes (top/heart/base) in simple terms
#                 - Describe longevity, projection, and best wearing occasions
#                 - Compare similar fragrances and highlight differences  
#                 - Recommend sizes (30ml for trying, 50ml standard, 100ml best value)
#                 - Suggest complementary products (travel sizes, gift sets)

#                 3. CUSTOMER ASSISTANCE:
#                 - Help find specific perfumes in our catalog
#                 - Provide detailed product information and customer reviews
#                 - Assist with gift recommendations for different recipients
#                 - Answer questions about shipping, returns, and policies
#                 - Help with order issues and tracking

#                 RECOMMENDATION PROCESS:
#                 1. Greet warmly: "Hi! I'm Aria, your perfume consultant. How can I help you find your perfect fragrance today?"
#                 2. Ask discovery questions to understand preferences
#                 3. Provide 2-3 tailored recommendations with explanations
#                 4. Help them decide and suggest purchase options
#                 5. Offer additional assistance

#                 SAMPLE RESPONSES:

#                 For beginners: "Since you're new to fragrances, I'd recommend starting with versatile, crowd-pleasing scents. Based on your preference for fresh scents, try..."

#                 For specific requests: "For a romantic date night fragrance, I suggest these options that are elegant and memorable..."

#                 For gifts: "For gifting to your wife who loves florals, these are safe yet special choices that most women adore..."

#                 COMMUNICATION STYLE:
#                 - Warm, enthusiastic but not pushy
#                 - Use fragrance terms but explain them simply
#                 - Ask follow-up questions to better understand needs
#                 - Be honest about budget constraints and offer alternatives
#                 - Acknowledge personal preferences vary due to skin chemistry

#                 ALWAYS INCLUDE:
#                 - Specific fragrance recommendations with reasons
#                 - Price ranges and size options when relevant
#                 - Occasion and season suitability
#                 - Similar alternatives if main choice unavailable
#                 - Invitation to ask more questions

#                 NEVER:
#                 - Recommend without understanding customer needs
#                 - Push expensive products inappropriately  
#                 - Make absolute claims about how fragrance will smell
#                 - Give medical advice about fragrances
#                 - Assume gender preferences for scents

#                 Your goal: Help every customer find their perfect fragrance match through personalized recommendations and excellent service.

#                 Customer message: ''' + user_prompt + '''

#                 Respond as Aria with helpful fragrance recommendations and assistance:
#                 ''' 
    
#     def Llama_model (self):
#         pass 
    
    
    
    # last sprint in this model ==>  1- vectordata base  2- LLM model 3- RAG pipline
    # integrate in  themodel prompt the username ,location ,  weather ,keywords ,user message and build your prompt 
    # and then pass it to the LLM model
    # NOW use the  model Gemini 2,5 pro to get the response
    # and return the response 
    #if needed store the prompt inthedatabase for further use or for building recommendation sys  or any other purpose
    
    
    