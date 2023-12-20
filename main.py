import os
os.environ['TOKENIZERS_PARALLELISM']= "False"
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI
from extract import extract_section_from_10q, extract_section_from_10k
from process_rag import build_rag_chain

def main():
    """
    Main execution function for the script.
    """
    # Set up API keys and initialize components
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Extract section from 10-Q filing
    filing_name = "apple"
    filing_url = "https://www.sec.gov/ix?doc=/Archives/edgar/data/320193/000032019323000077/aapl-20230701.htm"
    document_filename = extract_section_from_10q(filing_name, filing_url)
    
    # Extract section from 10-K filing
    filing_name = "accenture"
    filing_url = "https://www.sec.gov/Archives/edgar/data/1467373/000146737323000324/acn-20230831.htm"
    document_filename = extract_section_from_10k(filing_name, filing_url)

    # Ensure the document was successfully extracted before proceeding
    if document_filename is not None:
        embeddings = HuggingFaceEmbeddings()

        rag_chain = build_rag_chain(document_filename, embeddings, llm)
        question = "What are the sources of net sales or revenue? Breakdown in details"
        answer = rag_chain.invoke(question)
        with open("data/output/output.txt", "w") as f:
            f.write(filing_name+"\n")
            f.write(answer+"\n")
        print(answer)
    else:
        print("Failed to extract document.")

if __name__ == "__main__":
    main()