import pandas as pd 
from sentence_transformers import SentenceTransformer
from typing import List,Dict 

data = pd.read_csv("Chatbot\src\data\ecommerce_data.csv")

print(data.head())


sentenc_model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = sentenc_model.encode(data)


# next the vector db type ==>  chroma , qdrant , pinecone
# ازاي ارفع موديل فري سورس هيحتاج ايه وارفعه علي ايه 
# تحميل موديل شات تكلفته و تحميله وطريقه تنفيذه عشان ادخله سيرفس 
