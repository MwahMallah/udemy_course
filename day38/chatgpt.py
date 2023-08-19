import os 
import requests

user_input = input("Ask a question: ")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ.get('OPENAI_KEY')}"
}

params = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", 
                  "content": user_input
                  }],
    "temperature": 0.7
}

response = requests.post(url="https://api.openai.com/v1/completions", headers=headers, json=params)

print(response.json())