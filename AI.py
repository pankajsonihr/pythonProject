import openai

import API

openai.api_key = API.openai_api_key

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.8,
        max_tokens=150,
        n=1,
        stop=None,
    )
    return response.choices[0].text
