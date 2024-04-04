from dotenv import load_dotenv
from openai import OpenAI
import os

openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate(prompt):
    stream = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield (chunk.choices[0].delta.content)

def generate_summary(file):
    pass