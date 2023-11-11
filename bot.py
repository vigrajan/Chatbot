# bot.py
  
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "chat.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")


# Chatterbot is a combination of logic adapters & storage adapters. A text input is processed against multiple logic adapters & it returns a response & confidence interval. The highest confidence interval is the expected response. 
# Data is stored in storage adapters Ex: A SQL database 
# https://realpython.com/build-a-chatbot-python-chatterbot/#project-overview
# https://chatterbot.readthedocs.io/en/stable/
