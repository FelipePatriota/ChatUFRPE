import csv
import openai
import telebot
#Chave telegram: 6227139496:AAF4GJm87Sxep8-DO85OTOp7pwEgg9XinNU
# Substitua "sk-..." pela sua chave de API secreta
openai.api_key = "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"

# Escolha um modelo da open ai (por exemplo, davinci)
model = "text-davinci-003"

# Leia os arquivos CSV usando o módulo csv do python e armazene os dados em uma lista
data = []
for filename in ["Data/Data.csv", "Data2/Data2.csv", "Data3/Data3.csv"]:
  with open(filename, encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      data.append(row[0])

# Crie uma função que recebe uma pergunta do usuário e gera um texto usando o modelo da open ai


def generate_text(question):
  # Construa a entrada para a API da open ai com os dados do CSV e a pergunta do usuário
  input = "Dados:\n"
  for row in data:
    input += row + "\n"
  input += "\nPergunta: " + question + "\n\nResposta:"

  # Envie uma requisição para a API da open ai com os parâmetros desejados
  response = openai.Completion.create(
    engine=model,
    prompt=input,
    temperature=0.9,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"])

  # Retorne a resposta gerada pelo modelo
  return response["choices"][0]["text"]


# Teste a função com uma pergunta de exemplo
bot = telebot.TeleBot("6227139496:AAF4GJm87Sxep8-DO85OTOp7pwEgg9XinNU")


@bot.message_handler(func=lambda message: True)
def answer_question(message):
  question = message.text
  answer = generate_text(question)
  bot.send_message(message.chat.id, answer)


bot.polling()

