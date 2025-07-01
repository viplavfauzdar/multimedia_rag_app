from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document
import os

DB_PATH = "vectorstore/chroma_db"

def embed_and_store(texts, metadatas=None):
    embeddings = OpenAIEmbeddings()
    for i, text in enumerate(texts):
        print(f"[DEBUG] Chunk {i}: {text[:100]}")
    docs = [
        Document(page_content=text, metadata=metadatas[i] if metadatas else {})
        for i, text in enumerate(texts)
        if text.strip()
    ]
    if not docs:
        print("[WARNING] No valid text chunks to embed. Skipping Chroma upsert.")
        return
    db = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=DB_PATH)

def load_vectorstore():
    embeddings = OpenAIEmbeddings()
    return Chroma(persist_directory=DB_PATH, embedding_function=embeddings)

def get_query_embedding(query):
    embeddings = OpenAIEmbeddings()
    return embeddings.embed_query(query)