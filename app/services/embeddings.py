import openai
from app.core.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def embed(texts: list[str]) -> list[list[float]]:
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [d.embedding for d in response.data]
