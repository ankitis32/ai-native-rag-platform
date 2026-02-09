import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.indexes = {}
        self.documents = {}

    def get_index(self, tenant_id: str, dim: int):
        if tenant_id not in self.indexes:
            self.indexes[tenant_id] = faiss.IndexFlatL2(dim)
            self.documents[tenant_id] = []
        return self.indexes[tenant_id]

    def add(self, tenant_id, embeddings, docs):
        index = self.get_index(tenant_id, len(embeddings[0]))
        index.add(np.array(embeddings).astype("float32"))
        self.documents[tenant_id].extend(docs)

    def search(self, tenant_id, query_embedding, k=5):
        index = self.indexes.get(tenant_id)
        if not index:
            return []
        D, I = index.search(
            np.array([query_embedding]).astype("float32"), k
        )
        return [self.documents[tenant_id][i] for i in I[0] if i < len(self.documents[tenant_id])]
