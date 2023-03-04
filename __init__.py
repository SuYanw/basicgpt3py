import openai
import time

openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

print("Bem-vindo à Lanchonete! Como posso ajudar hoje?")

while True:
    user_input = input("> ")
    prompt = f"Usuário: {user_input}\nLanchobot: "
    response = generate_response(prompt)
    print(response)
    time.sleep(1) # wait for 1 second before generating next response