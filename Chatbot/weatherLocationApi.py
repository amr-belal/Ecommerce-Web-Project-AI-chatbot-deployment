######################################################
############### FOR Testing Purpose ##################
######################################################



# import geocoder  
# import requests 
# import os
# from dotenv import load_dotenv
# load_dotenv()


# g = geocoder.ip('me')

# print(g.latlng)
# print(g.address)
# print(g.country)
# print(g.city) 

# latLangList = g.latlng

# lat = latLangList[0]

# long = latLangList[1]

# userCountry = g.country
# userCity = g.city
# userAddress = g.address
# # getting location from latitude and longitude and User data location
# print(f'latitude {lat} , longitude {long} , city {userCity} , country {userCountry} , address {userAddress}')


# # get Api Weather key 
# API_KEY = os.environ.get("WEATHER_API_KEY")

# # print(API_KEY)

# # url = f"http://api.openweathermap.org/data/2.5/weather?q={userCountry}&appid={API_KEY}&units=metric"


# # response= requests.get(url)
# # data = response.json()
# # print(data)
# # print(f"Weather: {data['weather'][0]['description']}")
# # print(f"Temperature: {data['main']['temp']}°C")


# def get_current_location():
#     latLangList = g.latlng

#     lat = latLangList[0]

#     long = latLangList[1]

#     userCountry = g.country
#     userCity = g.city
#     userAddress = g.address
#     return [lat , long , userCity , userCountry , userAddress]

# def get_current_weather(loc):
#     API_KEY = os.environ.get("WEATHER_API_KEY")
#     url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={loc}"
#     response= requests.get(url)
#     data = response.json()
#     return [data["current"]["temp_c"] , data["current"]["condition"]["text"]]

# userCityAPI = get_current_location()
# print(get_current_weather(userCityAPI[2]))


# import requests

# def get_weather(city):
#     api_key = os.environ.get("WEATHER_API_KEY_2")
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     res = requests.get(url).json()
#     return res['weather'][0]['description']

# print(get_weather(g.city))




######################################################
############### FOR Testing Purpose ##################
######################################################







# import yake 
# def yake_keywords(text , lang="en" , top_n=5):
#     kw_extractor = yake.KeywordExtractor(lang=lang , n=2 ,top = top_n)
    
#     keywords = kw_extractor.extract_keywords(text)
#     return [kw for kw,score in keywords]


# msg = "I want to learn Python for data science and machine learning."
# print(yake_keywords(msg))



# # from keybert import KeyBERT 

# # kw_model  = KeyBERT()

# # def extract_keywords(text, top_n=5):
# #     keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english')
# #     return [kw for kw, score in keywords]

# # msg = "I want to learn Python for data science and machine learning."
# # print(extract_keywords(msg))


# #  it seems that the yake is similar to keybert in performance and  slightly better



import json

with open('FrontEnd_React\server\data.json') as f:
    data = json.load(f)

print(data["products"][0])



# import os
# import google.generativeai as genai  # ← FIXED: Correct import
# import json
# from typing import Optional, Dict, Any
# from dotenv import load_dotenv
# load_dotenv()

# class PerfumeShopChatbot:
#     def __init__(self):
#         self.API_KEY = None
#         self.model = None
#         self.conversation_history = []
    
#     def gemini_api(self, prompt: str, API_KEY: Optional[str] = None) -> str:
#         """
#         Complete Gemini API function for perfume shop chatbot
        
#         Args:
#             prompt (str): User's message/query
#             API_KEY (str, optional): Google API key, if not provided uses environment variable
            
#         Returns:
#             str: AI assistant response as perfume consultant
#         """
        
#         # Set API Key
#         if API_KEY:
#             self.API_KEY = API_KEY
#         else:
#             # FIXED: Check both possible environment variable names
#             self.API_KEY = os.environ.get("GEMENI_API_KEY") or os.environ.get("GEMENI_API_KEY")
        
#         # Check if API key exists
#         if not self.API_KEY:
#             return "❌ Error: Google API Key not found. Please set GEMENI_API_KEY or GOOGLE_API_KEY environment variable or pass API_KEY parameter."
        
#         try:
#             # FIXED: Configure Gemini API correctly
#             genai.configure(api_key=self.API_KEY)
            
#             # FIXED: Initialize the model correctly
#             self.model = genai.GenerativeModel(
#                 model_name='gemini-1.5-flash',  # Using more stable model
#                 generation_config=genai.types.GenerationConfig(
#                     temperature=0.7,
#                     top_p=0.8,
#                     top_k=40,
#                     max_output_tokens=1000,
#                 )
#             )
            
#             # Complete system prompt for perfume consultant
#             system_prompt = f'''
# You are Aria, an expert perfume consultant and shopping assistant for our premium online perfume boutique. You specialize in personalized fragrance recommendations and customer service.

# YOUR ROLE:
# - Expert perfume consultant with deep fragrance knowledge
# - Personal shopping assistant for perfume recommendations  
# - Customer service representative for our e-commerce platform
# - Friendly, knowledgeable, and professional advisor

# CORE RESPONSIBILITIES:

# 1. FRAGRANCE RECOMMENDATIONS:
#    - Analyze customer preferences and suggest perfect matches
#    - Ask qualifying questions: "What scents do you currently love?", "What occasions will you wear this for?", "Do you prefer fresh or intense fragrances?"
#    - Recommend based on: fragrance families, occasions, seasons, personality, budget
#    - Explain why each recommendation fits their needs
#    - Suggest 2-3 options with detailed explanations

# 2. PRODUCT EXPERTISE:
#    - Explain fragrance notes (top/heart/base) in simple terms
#    - Describe longevity, projection, and best wearing occasions
#    - Compare similar fragrances and highlight differences
#    - Recommend sizes (30ml for trying, 50ml standard, 100ml best value)
#    - Suggest complementary products (travel sizes, gift sets)

# 3. CUSTOMER ASSISTANCE:
#    - Help find specific perfumes in our catalog
#    - Provide detailed product information and customer reviews
#    - Assist with gift recommendations for different recipients
#    - Answer questions about shipping, returns, and policies
#    - Help with order issues and tracking

# FRAGRANCE FAMILIES KNOWLEDGE:
# - Fresh: Citrus, aquatic, green (light, energizing, daytime)
# - Floral: Rose, jasmine, peony (feminine, romantic, versatile)
# - Oriental: Vanilla, amber, spices (warm, sensual, evening)
# - Woody: Sandalwood, cedar, patchouli (sophisticated, unisex)
# - Gourmand: Chocolate, caramel, coffee (sweet, cozy, young)

# POPULAR RECOMMENDATIONS BY CATEGORY:
# - Office/Work: Light, fresh, not overpowering
# - Date Night: Sensual, memorable, sophisticated  
# - Casual Daily: Versatile, pleasant, moderate projection
# - Special Occasions: Luxurious, unique, statement-making
# - Gifts: Crowd-pleasing, classic, safe choices

# RECOMMENDATION PROCESS:
# 1. Greet warmly: "Hi! I'm Aria, your perfume consultant. How can I help you find your perfect fragrance today? 🌸"
# 2. Ask discovery questions to understand preferences
# 3. Provide 2-3 tailored recommendations with explanations
# 4. Help them decide and suggest purchase options
# 5. Offer additional assistance

# SAMPLE RESPONSES:

# For beginners: "Since you're new to fragrances, I'd recommend starting with versatile, crowd-pleasing scents. Based on your preference for fresh scents, try..."

# For specific requests: "For a romantic date night fragrance, I suggest these options that are elegant and memorable..."

# For gifts: "For gifting to someone who loves florals, these are safe yet special choices that most people adore..."

# COMMUNICATION STYLE:
# - Warm, enthusiastic but not pushy
# - Use fragrance terms but explain them simply  
# - Ask follow-up questions to better understand needs
# - Be honest about budget constraints and offer alternatives
# - Acknowledge personal preferences vary due to skin chemistry
# - Use emojis sparingly for warmth (🌸, 💐, ✨)

# ALWAYS INCLUDE:
# - Specific fragrance recommendations with reasons
# - Price ranges and size options when relevant
# - Occasion and season suitability
# - Similar alternatives if main choice unavailable
# - Invitation to ask more questions

# NEVER:
# - Recommend without understanding customer needs
# - Push expensive products inappropriately
# - Make absolute claims about how fragrance will smell
# - Give medical advice about fragrances
# - Assume gender preferences for scents

# Your goal: Help every customer find their perfect fragrance match through personalized recommendations and excellent service.

# Customer message: {prompt}

# Respond as Aria with helpful fragrance recommendations and assistance:
# '''
            
#             # FIXED: Generate response from Gemini correctly
#             response = self.model.generate_content(system_prompt)
            
#             # Extract the response text
#             if response and response.text:
#                 assistant_response = response.text.strip()
                
#                 # Store conversation history
#                 self.conversation_history.append({
#                     "user_message": prompt,
#                     "assistant_response": assistant_response,
#                     "timestamp": self._get_timestamp()
#                 })
                
#                 return assistant_response
#             else:
#                 return "I apologize, I'm having trouble generating a response right now. Please try again."
                
#         except Exception as e:
#             error_message = f"❌ Error communicating with Gemini API: {str(e)}"
#             print(f"Gemini API Error: {e}")  # For debugging
#             return f"I apologize, I'm experiencing technical difficulties. Please try again in a moment. If the problem persists, please contact support."
    
#     def _get_timestamp(self) -> str:
#         """Get current timestamp for conversation history"""
#         from datetime import datetime
#         return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
#     def get_conversation_history(self) -> list:
#         """Get the conversation history"""
#         return self.conversation_history
    
#     def clear_conversation_history(self):
#         """Clear the conversation history"""
#         self.conversation_history = []
    
#     def set_api_key(self, api_key: str):
#         """Set the Google API key"""
#         self.API_KEY = api_key
#         os.environ["GEMENI_API_KEY"] = api_key

# # ALTERNATIVE: Simpler implementation without complex configuration
# class SimplePerfumeChatbot:
#     def __init__(self):
#         self.conversation_history = []
    
#     def simple_gemini_api(self, prompt: str, API_KEY: Optional[str] = None) -> str:
#         """
#         Simplified Gemini API implementation
#         """
#         # Get API Key
#         api_key = API_KEY or os.environ.get("GEMENI_API_KEY") or os.environ.get("GEMENI_API_KEY")
        
#         if not api_key:
#             return "❌ Error: Google API Key not found."
        
#         try:
#             # Configure and create model
#             genai.configure(api_key=api_key)
#             model = genai.GenerativeModel('gemini-2.5-flash')
            
#             # Create the full prompt
#             full_prompt = f'''
# You are Aria, a friendly perfume consultant for our online perfume shop. Help customers find their perfect fragrance.

# Key Guidelines:
# - Ask about their preferences (fresh vs intense, occasions, budget)
# - Recommend 2-3 specific fragrances with explanations
# - Be warm and professional
# - Ask follow-up questions to understand their needs

# Customer says: "{prompt}"

# Respond as Aria:
# '''
            
#             # Generate response
#             response = model.generate_content(full_prompt)
            
#             if response and response.text:
#                 assistant_response = response.text.strip()
                
#                 # Store conversation
#                 self.conversation_history.append({
#                     "user": prompt,
#                     "assistant": assistant_response,
#                     "time": self._get_timestamp()
#                 })
                
#                 return assistant_response
#             else:
#                 return "I apologize, I couldn't generate a response. Please try again."
                
#         except Exception as e:
#             print(f"Error: {e}")
#             return "I'm experiencing technical difficulties. Please try again."
    
#     def _get_timestamp(self) -> str:
#         from datetime import datetime
#         return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # Usage Examples:
# if __name__ == "__main__":
#     print("Testing Perfume Shop Chatbot...")
#     print("=" * 50)
    
#     # Test the fixed implementation
#     chatbot = PerfumeShopChatbot()
    
#     # Test simple implementation as backup
#     simple_chatbot = SimplePerfumeChatbot()
    
#     test_messages = [
#         "Hi, I need a perfume for work",
#         "I need a gift for my girlfriend who loves sweet scents",
#         "Tell me about Chanel No. 5"
#     ]
    
#     for i, message in enumerate(test_messages, 1):
#         print(f"\n--- Test {i} ---")
#         print(f"User: {message}")
        
#         # Try main implementation first
#         response = chatbot.gemini_api(message)
#         if "technical difficulties" in response or "Error" in response:
#             # Fall back to simple implementation
#             print("Trying simple implementation...")
#             response = simple_chatbot.simple_gemini_api(message)
        
#         print(f"Aria: {response[:200]}...")
    
#     # Show conversation history
#     print("\n" + "=" * 50)
#     print("Conversation History:")
#     for i, conv in enumerate(chatbot.get_conversation_history(), 1):
#         print(f"\nConversation {i}:")
#         print(f"User: {conv['user_message']}")
#         print(f"Aria: {conv['assistant_response'][:100]}...")
#         print(f"Time: {conv['timestamp']}")

# # Quick test function
# def quick_test():
#     """Quick test to verify the fix works"""
#     chatbot = SimplePerfumeChatbot()
#     response = chatbot.simple_gemini_api("Hello, I need help choosing a perfume")
#     print(f"Quick test response: {response}")

# if __name__ == "__main__":
#     quick_test()
    


# ########################### RAG #####################################################


# import os
# import google.generativeai as genai
# import json
# import chromadb
# from sentence_transformers import SentenceTransformer
# from typing import Optional, Dict, Any, List
# from dotenv import load_dotenv
# from datetime import datetime
# import re

# load_dotenv()

# class PerfumeRAGSystem:
#     """
#     Complete RAG (Retrieval-Augmented Generation) system for perfume shop
#     Combines vector database with product knowledge and Gemini API
#     """
    
#     def __init__(self, db_path: str = "./perfume_vector_db"):
#         # Initialize vector database
#         self.client = chromadb.PersistentClient(path=db_path)
#         self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
#         # Create collection for perfume products
#         self.collection = self.client.get_or_create_collection(
#             name="perfume_products",
#             metadata={"hnsw:space": "cosine"}
#         )
        
#         # Initialize chatbot
#         self.chatbot = PerfumeShopChatbot()
#         self.conversation_history = []
        
#         print("✅ RAG System initialized successfully!")
    
#     def load_product_data(self, json_file_path: str):
#         """
#         Load perfume product data from JSON file into vector database
#         Expected format: {"products": [{"name": "", "description": "", ...}]}
#         """
#         try:
#             with open(json_file_path, 'r', encoding='utf-8') as f:
#                 data = json.load(f)
            
#             # Handle different JSON structures
#             if 'products' in data:
#                 products = data['products']
#             elif isinstance(data, list):
#                 products = data
#             else:
#                 products = [data]
            
#             self._process_and_store_products(products)
#             print(f"✅ Loaded {len(products)} products into RAG system")
            
#         except FileNotFoundError:
#             print(f"❌ Error: File {json_file_path} not found")
#         except json.JSONDecodeError:
#             print(f"❌ Error: Invalid JSON format in {json_file_path}")
#         except Exception as e:
#             print(f"❌ Error loading product data: {str(e)}")
    
#     def _process_and_store_products(self, products: List[Dict]):
#         """Process and store products in vector database"""
#         all_texts = []
#         all_metadatas = []
#         all_ids = []
        
#         for i, product in enumerate(products):
#             try:
#                 # Extract product information
#                 product_info = self._extract_product_info(product, i)
                
#                 if product_info['searchable_text']:
#                     all_texts.append(product_info['searchable_text'])
#                     all_metadatas.append(product_info['metadata'])
#                     all_ids.append(product_info['id'])
                    
#             except Exception as e:
#                 print(f"⚠️  Warning: Error processing product {i}: {str(e)}")
#                 continue
        
#         # Add to vector database in batches
#         if all_texts:
#             batch_size = 100
#             for i in range(0, len(all_texts), batch_size):
#                 batch_texts = all_texts[i:i + batch_size]
#                 batch_metadata = all_metadatas[i:i + batch_size]
#                 batch_ids = all_ids[i:i + batch_size]
                
#                 self.collection.add(
#                     documents=batch_texts,
#                     metadatas=batch_metadata,
#                     ids=batch_ids
#                 )
    
#     def _extract_product_info(self, product: Dict, index: int) -> Dict:
#         """Extract and format product information for RAG"""
#         # Get product name
#         name = product.get('name') or product.get('title') or f"Product {index}"
        
#         # Get description
#         description = product.get('description') or product.get('details') or ""
        
#         # Get brand
#         brand = product.get('brand') or product.get('manufacturer') or ""
        
#         # Get price
#         price = product.get('price') or product.get('cost') or 0
        
#         # Get category/type
#         category = product.get('category') or product.get('type') or ""
        
#         # Get fragrance notes
#         top_notes = product.get('top_notes') or product.get('topNotes') or []
#         middle_notes = product.get('middle_notes') or product.get('middleNotes') or []
#         base_notes = product.get('base_notes') or product.get('baseNotes') or []
        
#         # Get additional attributes
#         longevity = product.get('longevity') or ""
#         sillage = product.get('sillage') or product.get('projection') or ""
#         occasions = product.get('occasions') or []
#         season = product.get('season') or product.get('best_season') or ""
        
#         # Create searchable text combining all relevant information
#         searchable_parts = [
#             name,
#             brand,
#             description,
#             category,
#             f"Top notes: {', '.join(top_notes) if top_notes else ''}",
#             f"Middle notes: {', '.join(middle_notes) if middle_notes else ''}",
#             f"Base notes: {', '.join(base_notes) if base_notes else ''}",
#             f"Longevity: {longevity}",
#             f"Projection: {sillage}",
#             f"Occasions: {', '.join(occasions) if occasions else ''}",
#             f"Season: {season}"
#         ]
        
#         searchable_text = " ".join([part for part in searchable_parts if part.strip()])
        
#         # Create metadata
#         metadata = {
#             'name': name,
#             'brand': brand,
#             'price': float(price) if price else 0.0,
#             'category': category,
#             'top_notes': top_notes[:3] if top_notes else [],  # Limit for metadata
#             'middle_notes': middle_notes[:3] if middle_notes else [],
#             'base_notes': base_notes[:3] if base_notes else [],
#             'longevity': longevity,
#             'sillage': sillage,
#             'occasions': occasions[:3] if occasions else [],
#             'season': season,
#             'description_preview': description[:200] if description else ""
#         }
        
#         return {
#             'id': f"product_{index}_{name.replace(' ', '_').lower()}",
#             'searchable_text': searchable_text,
#             'metadata': metadata
#         }
    
#     def retrieve_relevant_products(self, query: str, n_results: int = 5) -> List[Dict]:
#         """Retrieve relevant products based on user query"""
#         try:
#             results = self.collection.query(
#                 query_texts=[query],
#                 n_results=n_results,
#                 include=['documents', 'metadatas', 'distances']
#             )
            
#             relevant_products = []
#             for i, (doc, metadata, distance) in enumerate(zip(
#                 results['documents'][0],
#                 results['metadatas'][0], 
#                 results['distances'][0]
#             )):
#                 relevant_products.append({
#                     'rank': i + 1,
#                     'relevance_score': 1 - distance,  # Convert distance to similarity
#                     'product_info': metadata,
#                     'matched_text': doc[:300] + "..." if len(doc) > 300 else doc
#                 })
            
#             return relevant_products
            
#         except Exception as e:
#             print(f"❌ Error retrieving products: {str(e)}")
#             return []
    
#     def generate_enhanced_prompt(self, user_query: str) -> str:
#         """Generate enhanced prompt with retrieved product information"""
#         # Retrieve relevant products
#         relevant_products = self.retrieve_relevant_products(user_query, n_results=3)
        
#         # Build product context
#         product_context = ""
#         if relevant_products:
#             product_context = "\n\nRELEVANT PRODUCTS FROM OUR CATALOG:\n"
#             for product in relevant_products:
#                 info = product['product_info']
#                 product_context += f"""
# **{info['name']}** by {info['brand']}
# - Price: ${info['price']:.2f}
# - Category: {info['category']}
# - Top Notes: {', '.join(info['top_notes']) if info['top_notes'] else 'Not specified'}
# - Middle Notes: {', '.join(info['middle_notes']) if info['middle_notes'] else 'Not specified'}
# - Base Notes: {', '.join(info['base_notes']) if info['base_notes'] else 'Not specified'}
# - Longevity: {info['longevity']}
# - Occasions: {', '.join(info['occasions']) if info['occasions'] else 'Versatile'}
# - Season: {info['season']}
# - Description: {info['description_preview']}
# - Relevance: {product['relevance_score']:.2f}
# ---"""
        
#         # Enhanced prompt with product knowledge
#         enhanced_prompt = f"""
# You are Aria, an expert perfume consultant for our premium online perfume boutique. You have access to our complete product catalog and specialize in personalized fragrance recommendations.

# YOUR ROLE:
# - Expert perfume consultant with deep fragrance knowledge
# - Access to specific product information from our inventory
# - Personal shopping assistant providing accurate product details
# - Customer service representative with real-time product availability

# IMPORTANT: When recommending products, ONLY suggest items from our catalog provided below. Always mention specific product names, brands, and accurate details from our inventory.

# {product_context}

# CUSTOMER QUERY: {user_query}

# GUIDELINES:
# - If relevant products are available, recommend specific items from our catalog with accurate details
# - Explain why each recommendation matches their needs based on the product specifications
# - Mention specific fragrance notes, longevity, and occasions from our product data
# - Include accurate pricing from our catalog
# - If no relevant products are found, ask clarifying questions to better understand their preferences
# - Always maintain your warm, professional consultant personality
# - Use the actual product information provided, don't make up details

# Respond as Aria with specific product recommendations from our catalog:
# """
        
#         return enhanced_prompt
    
#     def chat_with_rag(self, user_message: str, API_KEY: Optional[str] = None) -> str:
#         """
#         Main RAG chat function combining retrieval and generation
#         """
#         try:
#             # Generate enhanced prompt with product context
#             enhanced_prompt = self.generate_enhanced_prompt(user_message)
            
#             # Get response from Gemini with product context
#             response = self.chatbot.simple_gemini_api(enhanced_prompt, API_KEY)
            
#             # Store conversation with context
#             self.conversation_history.append({
#                 'user_message': user_message,
#                 'assistant_response': response,
#                 'retrieved_products': self.retrieve_relevant_products(user_message, 3),
#                 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             })
            
#             return response
            
#         except Exception as e:
#             print(f"❌ RAG Chat Error: {str(e)}")
#             return "I apologize, I'm experiencing technical difficulties with my product database. Please try again in a moment."
    
#     def get_product_by_name(self, product_name: str) -> Optional[Dict]:
#         """Get specific product information by name"""
#         try:
#             results = self.collection.query(
#                 query_texts=[product_name],
#                 n_results=1,
#                 include=['metadatas']
#             )
            
#             if results['metadatas'] and results['metadatas'][0]:
#                 return results['metadatas'][0][0]
#             return None
            
#         except Exception as e:
#             print(f"❌ Error finding product: {str(e)}")
#             return None
    
#     def search_products_by_criteria(self, 
#                                   price_range: tuple = None,
#                                   brand: str = None, 
#                                   category: str = None,
#                                   occasion: str = None) -> List[Dict]:
#         """Search products by specific criteria"""
#         # This would be enhanced with more sophisticated filtering
#         # For now, using text-based search
#         search_terms = []
        
#         if brand:
#             search_terms.append(f"brand {brand}")
#         if category:
#             search_terms.append(f"category {category}")
#         if occasion:
#             search_terms.append(f"occasion {occasion}")
#         if price_range:
#             search_terms.append(f"price between {price_range[0]} and {price_range[1]}")
        
#         search_query = " ".join(search_terms)
#         return self.retrieve_relevant_products(search_query, n_results=10)
    
#     def get_conversation_analytics(self) -> Dict:
#         """Get analytics about conversations and product recommendations"""
#         if not self.conversation_history:
#             return {"message": "No conversations yet"}
        
#         analytics = {
#             "total_conversations": len(self.conversation_history),
#             "most_recent_conversation": self.conversation_history[-1]['timestamp'],
#             "popular_products": {},
#             "common_queries": []
#         }
        
#         # Analyze product mentions
#         for conv in self.conversation_history:
#             for product in conv.get('retrieved_products', []):
#                 product_name = product['product_info']['name']
#                 analytics['popular_products'][product_name] = analytics['popular_products'].get(product_name, 0) + 1
        
#         return analytics

# class PerfumeShopChatbot:
#     """Enhanced version of the original chatbot for RAG integration"""
    
#     def __init__(self):
#         self.conversation_history = []
    
#     def simple_gemini_api(self, prompt: str, API_KEY: Optional[str] = None) -> str:
#         """Simplified Gemini API implementation for RAG integration"""
#         # Get API Key
#         api_key = API_KEY or os.environ.get("GEMENI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        
#         if not api_key:
#             return "❌ Error: Google API Key not found."
        
#         try:
#             # Configure and create model
#             genai.configure(api_key=api_key)
#             model = genai.GenerativeModel('gemini-1.5-flash')
            
#             # Generate response
#             response = model.generate_content(prompt)
            
#             if response and response.text:
#                 return response.text.strip()
#             else:
#                 return "I apologize, I couldn't generate a response. Please try again."
                
#         except Exception as e:
#             print(f"Gemini API Error: {e}")
#             return "I'm experiencing technical difficulties. Please try again."

# # Usage Examples and Testing
# if __name__ == "__main__":
#     print("🌸 Initializing Perfume RAG System...")
    
#     # Initialize RAG system
#     rag_system = PerfumeRAGSystem()
    
#     # Example product data (you can replace with your actual data.json)
#     example_products = {
#         "products": [
#             {
#                 "name": "Chanel No. 5",
#                 "brand": "Chanel",
#                 "price": 150.00,
#                 "category": "Classic Floral",
#                 "description": "The iconic fragrance with aldehydes, jasmine, and rose. A timeless classic that embodies elegance and sophistication.",
#                 "top_notes": ["Aldehydes", "Bergamot", "Lemon"],
#                 "middle_notes": ["Jasmine", "Rose", "Lily of the Valley"],
#                 "base_notes": ["Sandalwood", "Vanilla", "Amber"],
#                 "longevity": "8-10 hours",
#                 "sillage": "Strong",
#                 "occasions": ["Evening", "Special Events", "Formal"],
#                 "season": "Fall/Winter"
#             },
#             {
#                 "name": "Dior Sauvage",
#                 "brand": "Dior",
#                 "price": 120.00,
#                 "category": "Fresh Spicy",
#                 "description": "A radically fresh fragrance, Sauvage is both raw and noble. Inspired by wide-open spaces and blue skies.",
#                 "top_notes": ["Bergamot", "Pink Pepper"],
#                 "middle_notes": ["Sichuan Pepper", "Lavender", "Star Anise"],
#                 "base_notes": ["Ambroxan", "Cedar", "Labdanum"],
#                 "longevity": "6-8 hours",
#                 "sillage": "Moderate to Strong",
#                 "occasions": ["Casual", "Work", "Date Night"],
#                 "season": "All seasons"
#             },
#             {
#                 "name": "YSL Black Opium",
#                 "brand": "Yves Saint Laurent",
#                 "price": 110.00,
#                 "category": "Oriental Gourmand",
#                 "description": "A seductive gourmand floral fragrance with coffee, vanilla, and white flowers. Perfect for the modern, confident woman.",
#                 "top_notes": ["Pink Pepper", "Orange Blossom", "Pear"],
#                 "middle_notes": ["Coffee", "Jasmine", "Bitter Almond"],
#                 "base_notes": ["Vanilla", "Patchouli", "Cedar"],
#                 "longevity": "7-9 hours",
#                 "sillage": "Strong",
#                 "occasions": ["Evening", "Date Night", "Clubbing"],
#                 "season": "Fall/Winter"
#             }
#         ]
#     }
    
#     # Save example data
#     with open('perfume_products.json', 'w') as f:
#         json.dump(example_products, f, indent=2)
    
#     # Load product data into RAG system
#     rag_system.load_product_data('perfume_products.json')
    
#     # Test RAG chat
#     test_queries = [
#         "I need a perfume for work that's fresh and not too strong",
#         "What do you have from Chanel?",
#         "I want something sweet and gourmand for evening",
#         "Show me perfumes under $130",
#         "I need a gift for someone who likes classic scents"
#     ]
    
#     print("\n🧪 Testing RAG System:")
#     print("=" * 60)
    
#     for i, query in enumerate(test_queries, 1):
#         print(f"\n--- Test {i} ---")
#         print(f"👤 User: {query}")
        
#         # Get RAG response
#         response = rag_system.chat_with_rag(query)
#         print(f"🌸 Aria: {response[:300]}...")
        
#         # Show retrieved products
#         products = rag_system.retrieve_relevant_products(query, 2)
#         print(f"\n📦 Retrieved Products:")
#         for product in products:
#             info = product['product_info']
#             print(f"   • {info['name']} by {info['brand']} (${info['price']}) - Relevance: {product['relevance_score']:.2f}")
    
#     # Show analytics
#     print(f"\n📊 Analytics:")
#     analytics = rag_system.get_conversation_analytics()
#     print(f"   • Total Conversations: {analytics['total_conversations']}")
#     print(f"   • Popular Products: {analytics['popular_products']}")
    
#     print("\n✅ RAG System testing completed!")
    
    
    
