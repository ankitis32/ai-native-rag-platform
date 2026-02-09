import openai
from app.core.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def generate(prompt: str) -> str:
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
