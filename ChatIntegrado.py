import openai
import telebot
#https://replit.com/join/agnrlfszmg-valdirjunior4 
# Substitua "sk-..." pela sua chave de API secreta
openai.api_key = ""
bot = telebot.TeleBot("chave")

# Escolha um modelo da open ai (por exemplo, davinci)
model = "text-davinci-003"

# Leia o arquivo CSV usando o módulo csv do python
import csv
data = []
for filename in ["Data/Data.csv", "Data/Data2.csv", "Data/Data3.csv"]:
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
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )

    # Retorne a resposta gerada pelo modelo
    return response["choices"][0]["text"]

@bot.message_handler(func=lambda message: True)
def answer_question(message):
        question = message.text
        answer = generate_text(question)
        bot.send_message(message.chat.id, answer)

bot.polling()
