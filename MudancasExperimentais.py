import openai
import telebot
import csv

# Substitua "YOUR_API_KEY" pela sua chave de API secreta
openai.api_key = ""

# Escolha um modelo da OpenAI (por exemplo, "davinci")
model = "text-davinci-003"

# Leia os arquivos CSV usando o módulo csv do python e armazene os dados em uma lista
data = []
for filename in ["data1.csv", "data2.csv", "data3.csv", "data4.csv"]:
  with open(filename, encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      data.append(row[0])

# Crie uma função que recebe uma pergunta do usuário e gera um texto usando o modelo da OpenAI
def generate_text(question):
  # Construa a entrada para a API da OpenAI com os dados do CSV e a pergunta do usuário
  prompt = "Dados:\n"
  for row in data:
    prompt += row + "\n"
  prompt += "\nPergunta: " + question + "\n\nResposta:"

  # Envie uma requisição para a API da OpenAI com os parâmetros desejados
  response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
  )

  # Retorne a resposta gerada pelo modelo
  return response.choices[0].text.strip()

# Teste a função com uma pergunta de exemplo
bot = telebot.TeleBot()

@bot.message_handler(func=lambda message: True)
def answer_question(message):
  question = message.text
  answer = generate_text(question)
  bot.send_message(message.chat.id, answer)

bot.polling()
