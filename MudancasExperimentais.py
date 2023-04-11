import csv
import openai
import telebot
openai.api_key = ""
model = "text-davinci-003"
data1 = []
data2 = []
data3 = []
data4 = []
for filename in ["data1.csv", "data2.csv", "data3.csv", "data4.csv"]:
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if filename == "data1.csv":
                data1.append(row)
            elif filename == "data2.csv":
                data2.append(row)
            elif filename == "data3.csv":
                data3.append(row)
            elif filename == "data4.csv":
                data4.append(row)
def generate_text(question):
    questions = []
    answers = []
    print(f"Received question: {question}")
    for row in data1:
        if len(row) > 1:
            questions.append(row[0])
            answers.append(row[1])
    for row in data2:
        if len(row) > 1:
            questions.append(row[0])
            answers.append(row[1])
    for row in data3:
        if len(row) > 1:
            questions.append(row[0])
            answers.append(row[1])
    for row in data4:
        if len(row) > 1:
            questions.append(row[0])
            answers.append(row[1])
    qa_pairs = []
    for i in range(len(questions)):
        qa_pairs.append(questions[i] + " " + answers[i])
    qa_string = ""
    for i in range(len(qa_pairs)):
        qa_string += qa_pairs[i] + "\n"
    prompt = question + "\n" + qa_string
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n"])
    print(response)
    answer = response["choices"][0]["text"]
    print(f"Generated answer: {answer}")
    return answer
bot = telebot.TeleBot("")
@bot.message_handler(func=lambda message: True)
def on_message(message):
    question = message.text.lower()
    answer = generate_text(question)
    bot.send_message(message.chat.id, answer)
bot.polling()
