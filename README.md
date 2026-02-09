# AI-Native RAG Platform

Production-shaped Retrieval-Augmented Generation system designed for
multi-tenant SaaS environments. 

This repository focuses on **architecture and system design**, not UI polish.
It demonstrates how I approach building AI-native backend platforms.

## Key Features

- API-first FastAPI service
- Multi-tenant RAG architecture
- Async document ingestion
- Vector search with per-tenant isolation
- LLM abstraction layer
- Dockerized local setup

---

## Architecture

High-level architecture and design decisions are documented here:
- docs/architecture.md
- docs/tradeoffs.md

---

## API Endpoints
POST /ingest
POST /query

## Local Setup
docker-compose up --build

## Notes

Most of my recent production work (LLMs, RAG, analytics platforms)
has been delivered in enterprise environments and is not public.
This repository demonstrates my architectural approach and coding style.

## Design Philosophy
- Separation of concerns
- Swapable infra components
- Scales from single-tenant → SaaS
