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
