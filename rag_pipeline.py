import os
from groq import Groq

from vector_store import VectorStore
from prompt import SYSTEM_PROMPT


class RAGPipeline:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is not set."
            )

        self.client = Groq(api_key=api_key)

        self.vector_store = VectorStore()

        self.model = os.getenv(
            "GROQ_MODEL",
            "openai/gpt-oss-20b"
        )

    def create_index(self, chunks):

        self.vector_store.create(chunks)

    def ask(self, question):

        retrieved_chunks = self.vector_store.search(
            question,
            top_k=5
        )

        if not retrieved_chunks:
            return (
                "I could not find this information "
                "in the uploaded documents.",
                []
            )

        context_parts = []

        for chunk in retrieved_chunks:

            context_parts.append(
                f"""
Source: {chunk['source']}
Page: {chunk['page']}

Content:
{chunk['text']}
"""
            )

        context = "\n".join(context_parts)

        user_prompt = f"""
Context from uploaded documents:

{context}

User Question:
{question}

Answer the question only using the context above.
"""

        response = self.client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],

            temperature=0
        )

        answer = response.choices[0].message.content

        return answer, retrieved_chunks