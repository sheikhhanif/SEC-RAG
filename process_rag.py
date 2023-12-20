import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def load_documents(filename):
    """
    Load documents from a specified file.

    Args:
        filename (str): Path to the file containing documents.

    Returns:
        list: List of documents loaded from the file.
    """
    loader = TextLoader(filename)
    return loader.load()

def split_documents(documents, chunk_size=3000, chunk_overlap=500):
    """
    Split documents into smaller chunks using a specified chunk size and overlap.

    Args:
        documents (list): List of documents to split.
        chunk_size (int): Size of each chunk in characters.
        chunk_overlap (int): Number of characters to overlap between chunks.

    Returns:
        list: List of split document chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(documents)


def create_retriever(docs, embeddings):
    """
    Create a FAISS retriever from document chunks.

    Args:
        docs (list): List of document chunks.
        embeddings: Embeddings used for FAISS indexing.

    Returns:
        object: FAISS retriever object.
    """
    db = FAISS.from_documents(docs, embeddings)
    return db.as_retriever()


def build_rag_chain(filename, embeddings, llm):
    """
    Build a RAG chain for answering questions based on the context from documents.

    Args:
        filename (str): File containing the documents.
        embeddings: Embeddings for FAISS indexing.
        llm: Initialized language model object.

    Returns:
        object: RAG chain object for question answering.
    """
    documents = load_documents(filename)
    document_chunks = split_documents(documents)
    retriever = create_retriever(document_chunks, embeddings)

    template = """Answer the question based only on the following context:
    {context}

    Question: {question}

    Precisely, Breakdown the sources and sub-sources (if any) of revenue or sale  in latest.
    Your answer should include: total revenue or sale, percentage of reveneu from each sources respect to total revenue. Output as a json.
    """ 
    
    prompt = ChatPromptTemplate.from_template(template)

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain