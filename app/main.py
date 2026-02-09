from fastapi import FastAPI
from app.api import ingest, query, health

app = FastAPI(title="AI-Native RAG Platform")

app.include_router(health.router)
app.include_router(ingest.router, prefix="/ingest")
app.include_router(query.router, prefix="/query")
