# Financial Document Analysis Tool: Extract SEC filings using RAG

## Overview
This tool is designed to extract specific sections from financial documents (like 10-Q filings) and analyze them using a Retriever-Augmented Generation (RAG) approach. It extracts text from specified sections, processes the text, and then uses a combination of document retrieval and language model inference to answer complex queries about the content.

## Features
- **Extraction of Specific Document Sections**: Targeted extraction of sections like 'Part 1, Item 1' from 10-Q filings.
- **Text Processing and Splitting**: Splits large documents into manageable chunks for better processing.
- **FAISS-based Document Retrieval**: Leverages FAISS for efficient similarity-based retrieval of document sections.
- **Language Model Inference**: Uses OpenAI's GPT-3.5 model for generating insightful responses based on the context provided by retrieved documents.

## Prerequisites
- Python 3.x
- An API key for OpenAI GPT-3.5 and SEC extractor API

## Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/sheikhhanif/SEC-RAG.git
cd SEC-RAG
pip install -r requirements.txt
