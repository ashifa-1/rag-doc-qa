# RAG-Powered Document Question Answering System

##  Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** based on Document Question Answering system.  
The system allows users to ask natural language questions over a collection of **PDF and TXT documents** and generates answers that are **grounded in the retrieved documents**, along with **source citations**.

The goal of the project is to demonstrate how modern RAG pipelines combine:
- semantic document retrieval, and
- large language models (LLMs)

to produce accurate, explainable, and source-aware answers.

---

##  System Architecture and RAG Pipeline

The system follows a **modular RAG architecture**, where each stage of the pipeline is clearly separated.

###  High-Level Flow



Documents (PDF / TXT)

↓

Document Loaders

↓

Text Chunking (with overlap)

↓

Embedding Generation

↓

FAISS Vector Store

↓

Semantic Retrieval (Top-k)

↓

Prompt Construction

↓

LLM Answer Generation

↓
Answer + Source Citations


###  Component Explanation

- **Document Loaders**
  - Load text from PDF and TXT files.
  - Preserve metadata such as source file name and page number.

- **Chunking**
  - Large documents are split into fixed-size overlapping chunks.
  - This ensures manageable input size and preserves context.

- **Embeddings**
  - Each chunk is converted into a dense vector using a sentence-transformer model.
  - These embeddings capture semantic meaning.

- **Vector Store (FAISS)**
  - Embeddings are stored in an in-memory FAISS index.
  - Enables fast similarity search.

- **Retriever**
  - Given a user query, retrieves the top-k most relevant chunks based on semantic similarity.

- **Prompt Builder**
  - Constructs a prompt that includes only the retrieved context.
  - Prevents hallucination by grounding the LLM response.

- **Answer Generator**
  - Uses a local HuggingFace LLM to generate the final answer.
  - Answers are based strictly on retrieved content.

- **CLI Interface**
  - Provides a simple command-line interface for users to ask questions and receive answers with sources.

---

## 📁 Project Structure


![Structure of the project](image-1.png)

---

##  Environment Setup

###  Prerequisites

- Python **3.9 – 3.11**
- Git
- pip

---

###  Step 1: Clone the Repository

```bash
git clone https://github.com/ashifa-1/rag-doc-qa
```
```bash
cd rag-doc-qa
```

### Step 2: (Optional) Create a Virtual Environment

```bash
python -m venv venv
```
Activate it:

- Windows

```bash
venv\Scripts\activate
```

- Mac / Linux

```bash
source venv/bin/activate
```
### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```
### Step 4: Add Documents

- Place your documents here:

data/raw/pdfs/   → PDF files
data/raw/txts/   → TXT files


The system supports multiple documents and mixed formats.

## Running the Application

 Important: Always run the project from the root directory using module execution.

```bash
python -m src.main
```

On startup, the system will:

- Load documents

- Chunk text

- Generate embeddings

- Build the vector store

You will then see:

System ready. Ask your questions!

#### Example Usage
- Ask a Question

**Enter your question (or type 'exit'):** What problem does Retrieval-Augmented Generation (RAG) aim to solve in knowledge-
intensive NLP tasks?

**ANSWER:**

The retrieval component would "collapse" and learn to retrieve the same documents regardless of the input. 
The collapse could be due to a less-explicit requirement for factual knowledge in some tasks, or the longer target sequences, which could result in less informative gradients for the retriever.

 **SOURCES:**

[1] rag_doc.pdf (page 1)

[2] rag_doc.pdf (page 19)

[3] rag_doc.pdf (page 17)

[4] rag_doc.pdf (page 9)

[5] rag_doc.pdf (page 1)

[6] rag_doc.pdf (page 1)

#### Handling Unknown Questions

- If the information is not present in the documents:

***ANSWER:***
I don't know based on the provided documents.

SOURCES:

None


This behavior ensures no hallucination and maintains answer reliability.

