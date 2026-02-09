# Design Tradeoffs

This document outlines intentional tradeoffs made in this demo
and how they would evolve in production.

---

## Vector Store Choice

**Current:** FAISS (local, in-memory)

**Why:**
- Zero external dependencies
- Fast iteration
- Easy to reason about

**Tradeoff:**
- Not persistent
- Not horizontally scalable

**Production Upgrade:**
- Pinecone / Weaviate / Qdrant
- Tenant-based namespaces
- Metadata-level access control

---

## Async Processing

**Current:** Async functions + background tasks

**Why:**
- Keeps complexity low
- Demonstrates intent clearly

**Tradeoff:**
- Not fault tolerant
- No retries or DLQs

**Production Upgrade:**
- Celery / Temporal / Kafka
- Idempotent ingestion jobs

---

## Authentication

**Current:** API key → tenant resolver

**Why:**
- Simple mental model
- Easy to demonstrate multi-tenancy

**Tradeoff:**
- No user-level auth
- No RBAC

**Production Upgrade:**
- OAuth / JWT
- Role-based permissions
- Organization-level isolation

---

## Prompt Strategy

**Current:** Static prompt template

**Why:**
- Transparent
- Easy to audit and debug

**Tradeoff:**
- Limited reasoning control

**Production Upgrade:**
- Prompt versioning
- Tool calling / agents
- Context compression

---

## Observability

**Current:** Logging only

**Why:**
- Keep demo focused

**Production Upgrade:**
- Tracing (OpenTelemetry)
- Token + latency metrics
- Cost attribution per tenant

