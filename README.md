# NVIDIA NIM Demo - Retrieval-Augmented Generation (RAG) with Streamlit

NVIDIA NIM (NVIDIA Inference Microservices) is a platform designed to simplify deploying AI applications across various infrastructures, including cloud, data centers, and on-premises environments. It provides pre-built, optimized microservices to run high-performance models, including large language models (LLMs) and generative AI solutions, using NVIDIA's TensorRT, TensorRT-LLM, and other tools. NIM supports widely-used AI applications such as chatbots, virtual assistants, and retrieval-augmented generation (RAG) pipelines, offering developers flexible deployment options and control over data privacy and security.

Additionally, NIM integrates with popular AI frameworks like LangChain and Hugging Face, allowing for streamlined implementation in existing workflows. Through partnerships with major cloud providers and hardware manufacturers, enterprises can deploy these microservices with minimal configuration, ensuring low-latency, high-throughput inference for domain-specific needs​


This project demonstrates a Retrieval-Augmented Generation (RAG) application, leveraging NVIDIA's large language models (LLMs) and FAISS for high-performance question-answering based on document embeddings. Built with Streamlit, the app provides an interactive interface for ingesting documents, creating embeddings, and generating answers to user queries by retrieving and synthesizing relevant information.

Project Overview
This application allows users to ask questions based on documents ingested from a local directory (e.g., PDF files), which the system then analyzes using a RAG approach. The project leverages NVIDIA's LLMs and embedding models to efficiently retrieve relevant document chunks, feeding them to the language model for context-rich responses.

Key Features
Document Ingestion: Loads documents from a specified directory (e.g., PDFs) using PyPDFDirectoryLoader for preprocessing.
Text Splitting: Splits documents into manageable chunks using RecursiveCharacterTextSplitter (700-character chunks with 50-character overlap) to improve retrieval relevance and maintain context across sections.
Embeddings Creation: Converts text chunks into vector embeddings using NVIDIAEmbeddings, storing them in a FAISS index for fast similarity searches.
Question Answering: Uses NVIDIA’s LLM model, meta/llama3-70b-instruct, to generate accurate answers based on retrieved context from the document embeddings.
Retrieval-Augmented Generation (RAG): Combines document retrieval and language generation, using FAISS to identify relevant chunks and supplying them to the language model to form precise, context-aware responses.
Interactive Streamlit Interface: Provides a user-friendly interface for embedding documents, entering queries, and viewing both generated answers and the underlying document content that informed the response.


### Technologies Used
NVIDIA LLM & Embeddings: For high-quality embeddings and language model generation.
FAISS (Facebook AI Similarity Search): Efficient similarity search for embedding retrieval.
LangChain: Modular library used for chaining components like embeddings, text splitters, and document loaders.
Streamlit: Simple and interactive interface for document processing and question answering.

### Example Workflow
Embed Documents: Load and process documents by clicking "Documents Embedding."
Ask Questions: Enter a question in the text box to retrieve context-based answers.
View Results: See generated answers and the supporting document content.


### Future Enhancements
Extend document loaders for additional formats (e.g., Word, HTML).
Enhance document chunking methods for improved context relevance.
Integrate support for multiple LLMs and embedding models.




Link : https://build.nvidia.com/explore/discover

