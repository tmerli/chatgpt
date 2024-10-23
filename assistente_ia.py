import openai

# Certifique-se de ter a chave da API configurada
openai.api_key = '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'

response = openai.ChatCompletion.create(  # Corrigido para "ChatCompletion" com "C" maiúsculo
    model="gpt-4",  # Escolha o modelo
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Crie um plano de aula sobre sustentabilidade para alunos do ensino fundamental."}
    ],
    max_tokens=150
)

print(response['choices'][0]['message']['content'])
