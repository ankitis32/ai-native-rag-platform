class RAGPipeline:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    async def run(self, query: str, tenant_id: str):
        docs = await self.retriever.retrieve(query, tenant_id)
        context = "\n".join(d.page_content for d in docs)

        prompt = f"""
        Answer using the context below.
        Context:
        {context}

        Question:
        {query}
        """

        return await self.llm.generate(prompt)
