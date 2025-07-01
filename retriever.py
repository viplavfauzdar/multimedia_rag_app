from utils.embeddings import load_vectorstore, get_query_embedding
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate

def answer_query(query):
    db = load_vectorstore()
    embedding = get_query_embedding(query)
    docs = db.similarity_search_by_vector(embedding, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    prompt = PromptTemplate.from_template("Answer the question based on the documents: {context}\nQuestion: {question}")
    chain = create_stuff_documents_chain(llm, prompt)
    return chain.invoke({"context": docs, "question": query})