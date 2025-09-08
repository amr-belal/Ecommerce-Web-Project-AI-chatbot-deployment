# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_community.vectorstores import Chroma
# import json
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# load_dotenv()

# # embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
# API_KEY = os.environ["GEMENI_API_KEY"]

# genai.configure(api_key=API_KEY)

# embeddings_model = genai.GenerativeModel("models/embedding-001")


# # with open('FrontEnd_React\server\data.json') as f:
# #     data = json.load(f)

# # documents = data["products"]

# # texts = [ d["text"] for d in documents]
# # metadata = [{"id":d["id"]} for d in documents]
# # db = Chroma.from_texts(texts, embeddings, metadatas=metadata,collection_name="perfumes")
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_community.vectorstores import Chroma

# class PerRetreivalModel:
#     def __init__(self, data, api_key: str):
#         # embeddings جاهزة من لانجتشين
#         embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

#         texts = [f"{d['name']} - {d['description']}" for d in data]
#         metadatas = [{"id": d["id"], "name": d["name"], "price": d["price"], "category": d["category"]} for d in data]

#         # أنشئ Chroma مباشرة
#         self.db = Chroma.from_texts(
#             texts=texts,
#             embedding=embeddings,   # ✅ هنا object مش function
#             metadatas=metadatas,
#             collection_name="perfumes"
#         )

#     def retrieved_data(self, query: str):
#         results = self.db.similarity_search(query, k=3)
#         context = "\n".join(
#             [f"{r.metadata['name']} ({r.metadata['price']}$): {r.page_content}" for r in results]
#         )
#         return context


import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings

# --- Wrapper للـ Gemini embeddings ---
class GeminiEmbeddingWrapper(Embeddings):
    def __init__(self, model: str = "models/embedding-001"):
        self.model = model

    def embed_documents(self, texts):
        return [genai.embed_content(model=self.model, content=t)["embedding"] for t in texts]

    def embed_query(self, query):
        return genai.embed_content(model=self.model, content=query)["embedding"]

# --- Retrieval Model ---
class PerRetreivalModel:
    def __init__(self, data, api_key: str):
        genai.configure(api_key=api_key)  # ✅ هنا بيشتغل بالـ API Key العادي

        embeddings = GeminiEmbeddingWrapper()

        texts = [f"{d['name']} - {d['description']}" for d in data]
        metadatas = [
            {
                "id": d["id"],
                "name": d["name"],
                "price": d["price"],
                "category": d["category"],
            }
            for d in data
        ]

        # ✅ بدل Chroma → FAISS
        self.db = FAISS.from_texts(
            texts=texts,
            embedding=embeddings,
            metadatas=metadatas
        )

    def retrieved_data(self, query: str):
        results = self.db.similarity_search(query, k=3)
        context = "\n".join(
            [f"{r.metadata['name']} ({r.metadata['price']}$): {r.page_content}" for r in results]
        )
        return context
