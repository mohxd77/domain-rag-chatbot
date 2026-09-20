import streamlit as st
from dotenv import load_dotenv

from document_loader import (
    extract_text_from_pdfs,
    split_documents
)

from rag_pipeline import RAGPipeline


load_dotenv()


st.set_page_config(
    page_title="Domain-Specific RAG Chatbot",
    page_icon="📚",
    layout="wide"
)


st.title("📚 Domain-Specific RAG Chatbot")

st.write(
    "Upload PDF documents and ask questions "
    "based on their content."
)


# Session state
if "pipeline" not in st.session_state:
    st.session_state.pipeline = None

if "processed" not in st.session_state:
    st.session_state.processed = False

if "messages" not in st.session_state:
    st.session_state.messages = []


# Sidebar
with st.sidebar:

    st.header("📄 Upload Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.write("Uploaded files:")

        for file in uploaded_files:
            st.write(f"• {file.name}")

    process_button = st.button(
        "🔄 Process Documents"
    )

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()


# Process documents
if process_button:

    if not uploaded_files:

        st.warning(
            "Please upload at least one PDF."
        )

    else:

        with st.spinner(
            "Processing documents..."
        ):

            try:

                documents = extract_text_from_pdfs(
                    uploaded_files
                )

                if not documents:

                    st.error(
                        "No readable text was found "
                        "in the uploaded PDFs."
                    )

                else:

                    chunks = split_documents(
                        documents
                    )

                    pipeline = RAGPipeline()

                    pipeline.create_index(
                        chunks
                    )

                    st.session_state.pipeline = pipeline
                    st.session_state.processed = True

                    st.success(
                        f"Documents processed successfully! "
                        f"{len(chunks)} chunks created."
                    )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )


# Chat
if st.session_state.processed:

    st.subheader("💬 Ask Questions")

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

    question = st.chat_input(
        "Ask something about your documents..."
    )

    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):

            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner(
                "Searching documents..."
            ):

                answer, sources = (
                    st.session_state.pipeline.ask(
                        question
                    )
                )

            st.markdown(answer)

            if sources:

                st.markdown(
                    "### 📌 Sources"
                )

                shown_sources = set()

                for source in sources:

                    source_key = (
                        source["source"],
                        source["page"]
                    )

                    if source_key not in shown_sources:

                        st.write(
                            f"📄 {source['source']} "
                            f"— Page {source['page']}"
                        )

                        shown_sources.add(
                            source_key
                        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

else:

    st.info(
        "👈 Upload one or more PDF files "
        "and click 'Process Documents' to begin."
    )