from fastapi import APIRouter, Header
from app.tenants.resolver import resolve_tenant
from app.services.embeddings import embed
from app.services.vector_store import VectorStore

router = APIRouter()
vector_store = VectorStore()

@router.post("/")
async def ingest(
    documents: list[str],
    x_api_key: str = Header(...)
):
    tenant_id = resolve_tenant(x_api_key)
    embeddings = embed(documents)
    vector_store.add(tenant_id, embeddings, documents)
    return {"status": "ingested", "count": len(documents)}
