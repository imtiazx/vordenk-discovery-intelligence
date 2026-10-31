import os

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    base_url="https://api.meta.ai/v1",
    api_key=os.environ["MODEL_API_KEY"],
)

response = client.chat.completions.create(
    model="muse-spark-1.3",
    messages=[
        {
            "role": "user",
            "content": "What are three differences between TDP and UDP?",
        },
    ],
)

print(response.model_dump_json(indent=2))