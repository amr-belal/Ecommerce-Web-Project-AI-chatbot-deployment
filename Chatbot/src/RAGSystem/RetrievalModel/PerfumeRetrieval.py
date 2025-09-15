# # from langchain_google_genai import GoogleGenerativeAIEmbeddings
# # from langchain_community.vectorstores import Chroma
# # import json
# # import google.generativeai as genai
# # import os
# # from dotenv import load_dotenv
# # load_dotenv()

# # # embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
# # API_KEY = os.environ["GEMENI_API_KEY"]

# # genai.configure(api_key=API_KEY)

# # embeddings_model = genai.GenerativeModel("models/embedding-001")


# # # with open('FrontEnd_React\server\data.json') as f:
# # #     data = json.load(f)

# # # documents = data["products"]

# # # texts = [ d["text"] for d in documents]
# # # metadata = [{"id":d["id"]} for d in documents]
# # # db = Chroma.from_texts(texts, embeddings, metadatas=metadata,collection_name="perfumes")
# # from langchain_google_genai import GoogleGenerativeAIEmbeddings
# # from langchain_community.vectorstores import Chroma

# # class PerRetreivalModel:
# #     def __init__(self, data, api_key: str):
# #         # embeddings جاهزة من لانجتشين
# #         embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# #         texts = [f"{d['name']} - {d['description']}" for d in data]
# #         metadatas = [{"id": d["id"], "name": d["name"], "price": d["price"], "category": d["category"]} for d in data]

# #         # أنشئ Chroma مباشرة
# #         self.db = Chroma.from_texts(
# #             texts=texts,
# #             embedding=embeddings,   # ✅ هنا object مش function
# #             metadatas=metadatas,
# #             collection_name="perfumes"
# #         )

# #     def retrieved_data(self, query: str):
# #         results = self.db.similarity_search(query, k=3)
# #         context = "\n".join(
# #             [f"{r.metadata['name']} ({r.metadata['price']}$): {r.page_content}" for r in results]
# #         )
# #         return context


# import google.generativeai as genai
# from langchain_community.vectorstores import FAISS
# from langchain_core.embeddings import Embeddings

# # --- Wrapper للـ Gemini embeddings ---
# class GeminiEmbeddingWrapper(Embeddings):
#     def __init__(self, model: str = "models/embedding-001"):
#         self.model = model

#     def embed_documents(self, texts):
#         return [genai.embed_content(model=self.model, content=t)["embedding"] for t in texts]

#     def embed_query(self, query):
#         return genai.embed_content(model=self.model, content=query)["embedding"]

# # --- Retrieval Model ---
# class PerRetreivalModel:
#     def __init__(self, data, api_key: str):
#         genai.configure(api_key=api_key) 

#         embeddings = GeminiEmbeddingWrapper()

#         texts = [f"{d['name']} - {d['description']}" for d in data]
#         metadatas = [
#             {
#                 "id": d["id"],
#                 "name": d["name"],
#                 "price": d["price"],
#                 "category": d["category"],
#             }
#             for d in data
#         ]

    
#         self.db = FAISS.from_texts(
#             texts=texts,
#             embedding=embeddings,
#             metadatas=metadatas
#         )

#     def retrieved_data(self, query: str):
#         results = self.db.similarity_search(query, k=3)
#         context = "\n".join(
#             [f"{r.metadata['name']} ({r.metadata['price']}$): {r.page_content}" for r in results]
#         )
#         return context
import os
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer


# # --- Wrapper للـ Gemini embeddings مع Batching ---
# class GeminiEmbeddingWrapper(Embeddings):
#     def __init__(self, model: str = "models/embedding-001", batch_size: int = 20):
#         self.model = model
#         self.batch_size = batch_size

#     def embed_documents(self, texts):
#         embeddings = []
#         for i in range(0, len(texts), self.batch_size):
#             batch = texts[i:i + self.batch_size]
#             for t in batch:
#                 emb = genai.embed_content(model=self.model, content=t)["embedding"]
#                 embeddings.append(emb)
#         return embeddings

#     def embed_query(self, query):
#         return genai.embed_content(model=self.model, content=query)["embedding"]

# # --- Retrieval Model ---
# class PerRetreivalModel:
#     def __init__(self, data, api_key: str, index_path: str = "perfumes_index"):
#         # Configure Gemini API
#         genai.configure(api_key=api_key) 
#         embeddings = GeminiEmbeddingWrapper()

#         # Load FAISS index if exists
#         if os.path.exists(index_path):
#             self.db = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
#         else:
#             # Prepare texts and metadata
#             texts = [f"{d['name']} - {d['description']}" for d in data]
#             metadatas = [
#                 {
#                     "id": d["id"],
#                     "name": d["name"],
#                     "price": d["price"],
#                     "category": d["category"],
#                 }
#                 for d in data
#             ]

#             # Create FAISS DB
#             self.db = FAISS.from_texts(
#                 texts=texts,
#                 embedding=embeddings,
#                 metadatas=metadatas
#             )

#             # Save FAISS index locally
#             self.db.save_local(index_path)

#     def retrieved_data(self, query: str):
#         results = self.db.similarity_search(query, k=3)
#         context = "\n".join(
#             [f"{r.metadata['name']} ({r.metadata['price']}$): {r.page_content}" for r in results]
#         )
#         return context


class PerfumeRetrievalFAISS:
    def __init__(self, index_path="perfume.index", metadata_path="metadata.json", model_name="all-MiniLM-L6-v2"):
        self.index = faiss.read_index(index_path)
        with open(metadata_path, "r") as f:
            self.metadatas = json.load(f)
        self.embedding_model = SentenceTransformer(model_name)

    def search(self, query: str, top_k: int = 3):
        q_emb = self.embedding_model.encode([query], convert_to_numpy=True)
        q_emb = q_emb / np.linalg.norm(q_emb, axis=1, keepdims=True)

        distances, indices = self.index.search(q_emb, top_k)

        results = []
        for idx, dist in zip(indices[0], distances[0]):
            meta = self.metadatas[idx]
            results.append({
                "id": meta["id"],
                "name": meta["name"],
                "description": meta["description"],
                "perfume_type": meta["perfume_type"],
                "price": meta["price"],
                "perfume_category": meta["perfume_category"],
                "image_link": meta["image_link"],
                "rating": meta["rating"],
                "count": meta["count"],
                "category": meta["category"],
                "score": float(dist)
            })
        return results