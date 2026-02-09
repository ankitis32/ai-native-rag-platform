from app.services.embeddings import embed
from app.services.llm import generate

class RAGPipeline:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    async def query(self, tenant_id: str, question: str):
        q_embedding = embed([question])[0]
        docs = self.vector_store.search(tenant_id, q_embedding)

        context = "\n".join(docs)

        prompt = f"""
You are an assistant answering questions using the context below.

Context:
{context}

Question:
{question}
"""
        return await generate(prompt)
