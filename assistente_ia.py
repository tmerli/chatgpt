import openai

# Certifique-se de ter a chave da API configurada
openai.api_key = 'sk-0MPuV5qQ4K-Q0nThOIehyH4kKEAvM0xbWZePD-RmmyT3BlbkFJ8P4SXf1dygtRtVJyBz78M_YhUurGBev7bVM4olW4oA'

response = openai.ChatCompletion.create(  # Corrigido para "ChatCompletion" com "C" maiúsculo
    model="gpt-4",  # Escolha o modelo
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Crie um plano de aula sobre sustentabilidade para alunos do ensino fundamental."}
    ],
    max_tokens=150
)

print(response['choices'][0]['message']['content'])
