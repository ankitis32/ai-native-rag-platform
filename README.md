# AI-Native RAG Platform

Production-shaped Retrieval-Augmented Generation system designed for
multi-tenant SaaS environments.

## Features
- Multi-tenant RAG architecture
- Async document ingestion
- Vector search with metadata filtering
- LLM provider abstraction
- API-first design (FastAPI)

## Architecture
[short explanation + link to docs/architecture.md]

## API Endpoints
POST /ingest
POST /query

## Local Setup
docker-compose up --build

## Design Philosophy
- Separation of concerns
- Swapable infra components
- Scales from single-tenant → SaaS
