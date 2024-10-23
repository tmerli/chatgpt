
import openai

# Configuração da chave da API
openai.api_key = 'org-dIJwVnOXt46CahkMknGoWQRU'

# Fazer uma solicitação ao GPT
response = openai.Completion.create(
  engine="gpt-4",  # Escolha o modelo (pode ser "gpt-3.5-turbo" ou outro disponível)
  prompt="Crie um plano de aula sobre sustentabilidade para alunos do ensino fundamental.",
  max_tokens=150  # Número máximo de tokens (palavras) gerados
)

# Exibir a resposta gerada pelo GPT
print(response.choices[0].text.strip())
