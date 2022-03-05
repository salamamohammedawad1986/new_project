from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#bot = ChatBot('Normal')

# the database parameter is use specify the path to the database


chatbot = ChatBot('edureka')
trainer = ListTrainer(chatbot)
trainer.train(['Hi, can I Help you find a course','sure I d love to find you a course'])

reponse = chatbot.get_response('I want a course')
print(response)



