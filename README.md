# AI-Native RAG Platform

Production-shaped Retrieval-Augmented Generation system designed for
multi-tenant SaaS environments. This repo demonstrates how I design AI-native, multi-tenant systems.

## Features
- Multi-tenant RAG architecture
- Async document ingestion
- Vector search with metadata filtering
- LLM provider abstraction
- API-first design (FastAPI)

## Architecture
docs/architecture.md

## API Endpoints
POST /ingest
POST /query

## Local Setup
docker-compose up --build

## Design Philosophy
- Separation of concerns
- Swapable infra components
- Scales from single-tenant → SaaS
