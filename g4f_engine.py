import random
from g4f.client import Client

gpt_client = Client()

async def get_neuro_comment(message_text):
    with open("prompt.txt", "r", encoding="utf-8") as file:
        prompt = file.read( )

    print(prompt)
    response = gpt_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"{prompt} '{message_text}'"}]
    )
    return response.choices[0].message.content