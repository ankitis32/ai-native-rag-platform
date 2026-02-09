# Architecture Overview

This repository demonstrates a production-shaped, AI-native
Retrieval-Augmented Generation (RAG) system designed with
multi-tenant SaaS environments in mind.

The goal is to show *system design thinking*, not just LLM API usage.

---

## High-Level Flow

Client → FastAPI → RAG Pipeline → LLM → Response

---

## Key Architectural Principles

### 1. API-First Design
- No notebooks
- Everything is accessible via HTTP APIs
- Enables frontend, agents, or other services to integrate cleanly

---

### 2. Multi-Tenant by Default
Each request is associated with a `tenant_id` resolved from an API key.

Tenant isolation is enforced at:
- Vector store namespace level
- Metadata filtering
- Ingestion boundaries

This mirrors real SaaS constraints.

---

### 3. Separation of Concerns

| Layer | Responsibility |
|-----|----------------|
| API | Validation, auth, request routing |
| Services | Core business logic |
| RAG Pipeline | Orchestration |
| Vector Store | Storage + retrieval |
| LLM Layer | Provider abstraction |

This allows:
- Model swapping
- Infra evolution
- Easier testing

---

### 4. Async Ingestion Path

Document ingestion runs asynchronously to avoid blocking user requests.
In production this would be handled by:
- Celery / Temporal / SQS
- Dedicated workers

Here it is intentionally lightweight.

---

## Scaling Considerations

| Component | Scale Path |
|--------|------------|
| Vector Store | FAISS → Pinecone / Weaviate |
| LLM | OpenAI → Anthropic → Self-hosted |
| Workers | Async tasks → Distributed queues |
| Auth | API keys → IAM / OAuth |

---

## What This Repo Is (and Isn’t)

**This is:**
- A realistic service skeleton
- Designed for SaaS evolution
- Opinionated but extensible

**This is not:**
- A UI-heavy demo
- A research notebook
- A toy script
