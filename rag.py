from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vector_db = Chroma(
    collection_name="research_memory",
    embedding_function=embeddings,
    persist_directory="./memory_db"
)


def store_documents(text):

    docs = [Document(page_content=text)]

    vector_db.add_documents(docs)


def retrieve_documents(query):

    results = vector_db.similarity_search(query, k=3)

    return "\n\n".join([r.page_content for r in results])