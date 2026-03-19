import openai

openai.api_key = "YOUR_API_KEY"   # replace with your key

def generate_question(role):
    prompt = f"Generate one interview question for a {role}."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message['content']


def evaluate_answer(question, answer):
    prompt = f"""
    Question: {question}
    Answer: {answer}

    Evaluate this answer. Give:
    1. Score out of 10
    2. Short feedback
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message['content']
