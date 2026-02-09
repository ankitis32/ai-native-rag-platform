from fastapi import APIRouter, Header
from app.tenants.resolver import resolve_tenant
from app.services.vector_store import VectorStore
from app.services.rag_pipeline import RAGPipeline

router = APIRouter()
vector_store = VectorStore()
rag = RAGPipeline(vector_store)

@router.post("/")
async def query(
    question: str,
    x_api_key: str = Header(...)
):
    tenant_id = resolve_tenant(x_api_key)
    answer = await rag.query(tenant_id, question)
    return {"answer": answer}
