import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

key = os.getenv("API_KEY")
client = OpenAI(api_key = key)

def load_json():
    with open('history.json', 'r') as f:
        data = json.load(f)
    return data

def write_json(data, file):
    with open(f'{file}.json', 'w') as f:
        json.dump(data, f, indent=4)

def get_messages():
    prev_messages = load_json()

    return prev_messages["Messages"]

def add_message(message, role):
    prev_messages = load_json()
    resp_val = {"role": role, "content": message}
    prev_messages["Messages"].append(resp_val)
    write_json(prev_messages, "history")

def send_prompt(message):
    prev_messages = load_json()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Youre a helpful assistant" },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    message_val = {"role": "user", "content": message}
    prev_messages["Messages"].append(message_val)

    resp = completion.choices[0].message.content
    resp_val = {"role": "system", "content": resp}
    prev_messages["Messages"].append(resp_val)

    write_json(prev_messages, "history")
    return resp

def new_chat():
    write_json({"Messages": []}, "history")

def prev_message():
    prev_messages = load_json()
    last_three = prev_messages[-3:]
    pre_prompt(last_three)

def pre_prompt(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}
        ]
    )
    return completion.choices[0].message.content