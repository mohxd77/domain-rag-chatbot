from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def extract_text_from_pdfs(uploaded_files):
    documents = []

    for uploaded_file in uploaded_files:
        reader = PdfReader(uploaded_file)

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()

            if text and text.strip():
                documents.append({
                    "text": text.strip(),
                    "source": uploaded_file.name,
                    "page": page_number
                })

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120
    )

    chunks = []

    for document in documents:
        split_texts = splitter.split_text(document["text"])

        for text in split_texts:
            chunks.append({
                "text": text,
                "source": document["source"],
                "page": document["page"]
            })

    return chunks