# Domain-Specific RAG Chatbot for PDF Question Answering

## 1. Project Overview

The Domain-Specific RAG Chatbot is a document question-answering application that allows users to upload PDF documents and ask questions about their contents.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate answers based only on the retrieved document context.

The application is built using Python and Streamlit.

## 2. Project Objective

The main objective of this project is to build a reliable question-answering system that can:

- Accept PDF documents from users.
- Extract text from PDF pages.
- Split extracted text into smaller chunks.
- Convert text chunks into numerical embeddings.
- Store embeddings in a FAISS vector database.
- Retrieve relevant document chunks for a user question.
- Generate an answer using a Large Language Model.
- Display the source document and page number.
- Avoid inventing information when the answer is not available in the uploaded documents.

## 3. Features

- PDF document upload
- Multiple PDF support
- PDF text extraction
- Text chunking
- Sentence Transformer embeddings
- FAISS vector similarity search
- Groq Large Language Model integration
- Context-based question answering
- Source document and page display
- Chat history
- Clear chat option
- Refusal when information is unavailable
- Streamlit web interface

## 4. Technologies Used

| Component | Technology |
|---|---|
| Programming Language | Python |
| PDF Extraction | pypdf |
| Text Splitting | LangChain Text Splitters |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | FAISS |
| Language Model | Groq |
| User Interface | Streamlit |
| Environment Variables | python-dotenv |
| Version Control | Git and GitHub |

## 5. RAG Workflow

```text
Upload PDF
     ↓
Extract Text
     ↓
Split Text into Chunks
     ↓
Create Embeddings
     ↓
Store Embeddings in FAISS
     ↓
User Asks Question
     ↓
Create Question Embedding
     ↓
Retrieve Relevant Chunks
     ↓
Send Context + Question to Groq
     ↓
Generate Grounded Answer
     ↓
Display Answer + Source/Page
```

## 6. Project Structure

```text
domain_rag_chatbot/
│
├── documents/
│   └── rag_test_document.pdf
│
├── tests/
│   └── test_questions.csv
│
├── vector_store/
│
├── app.py
├── document_loader.py
├── prompt.py
├── rag_pipeline.py
├── vector_store.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 7. Installation
Step 1: Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>

Move into the project directory:
cd domain_rag_chatbot

Step 2: Create a Virtual Environment
python -m venv venv

Activate the virtual environment on Windows:
venv\Scripts\activate

Step 3: Install Dependencies
pip install -r requirements.txt

## 8. API Key Configuration
This project uses the Groq API for answer generation.
Create a .env file in the project root:
GROQ_API_KEY=your_groq_api_key_here

## 9. Running the Application
Start the Streamlit application using:
streamlit run app.py
After starting the application, Streamlit will provide a local URL such as:
http://localhost:8501

Open the URL in a web browser.

## 10. How to Use the Application

Step 1
Open the Streamlit application.
Step 2
Upload one or more PDF documents using the upload section.
Step 3
Click:
Process Documents
The system will:
Extract PDF text.
Split the text into chunks.
Generate embeddings.
Store the embeddings in FAISS.
Step 4
Enter a question related to the uploaded documents.
Step 5
The system retrieves the most relevant document chunks and sends them to the Groq language model.
Step 6
The chatbot displays:
Answer
Source document
Page number

## 11. Example
Question
What are the library timings?
Answer
The college library is open from 9:00 AM to 5:00 PM on working days.
Source
rag_test_document.pdf — Page 1

## 12. Handling Unavailable Information
The chatbot is designed not to invent information.
For example, if the uploaded document does not contain information about the college principal and the user asks:
Who is the principal of the college?
The chatbot responds:
I could not find this information in the uploaded documents.
This helps keep answers grounded in the uploaded documents.
## 13. Testing
The project includes a testing file:
tests/test_questions.csv
The testing dataset contains 15 questions covering:
Questions whose answers are available in the document.
Questions whose answers are not available.
Source document verification.
Page number verification.
Refusal behavior.

The system is evaluated based on:
Retrieval accuracy
Answer correctness
Groundedness
Refusal quality
Source quality
Response time

## 14. Responsible AI and Security
The following security practices are followed:
API keys are stored in environment variables.
API keys are not included in source code.
The .env file is excluded from GitHub.
Confidential documents should not be uploaded without permission.
The chatbot does not intentionally invent information.
Users should verify information used for high-stakes decisions.
Instructions contained inside uploaded documents should not override the chatbot's system rules.
Uploaded files are restricted to PDF documents. 

## 15. Limitations
The system works best with text-based PDFs.
Scanned PDFs may require OCR support.
Retrieval quality depends on the quality and structure of the uploaded document.
Generated answers depend on the retrieved context.
The system may not correctly answer questions when relevant information cannot be retrieved.
High-stakes information should be independently verified.

## 16. Future Enhancements
Possible future improvements include:
OCR support for scanned PDFs
Multiple document collections
Document filtering
Conversation memory
User login and access control
Feedback buttons
FastAPI backend
Docker deployment
Improved evaluation using a larger question-answer dataset

## 17. Author
Name: Muhammad N
Project: Domain-Specific RAG Chatbot for PDF Question Answering 
Program: B.Tech Computer Science and Engineering
Project Type: Major Project

## 18. License
This project was developed for educational and academic purposes.