import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_question(role):
    prompt = f"Generate one interview question for a {role}."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def evaluate_answer(question, answer):
    prompt = f"""
Question: {question}
Answer: {answer}

Give:
1. Score out of 10
2. Short feedback
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
