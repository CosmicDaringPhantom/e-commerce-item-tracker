import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

key = os.getenv("API_KEY")
client = OpenAI(api_key = key)

def send_prompt(message):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": message
            }
        ]
    )

    print("loading answer.....")
    return completion.choices[0].message.content

def pre_prompting(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
        ]
    )

    return completion.choices[0].message.content

