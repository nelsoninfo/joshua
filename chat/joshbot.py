# -*- coding: utf-8 -*-


#chatbot imports
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

import logging
logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
	'Joshua',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	logic_adapters=[
		'chatterbot.logic.BestMatch',
		'chatterbot.logic.MathematicalEvaluation',
		#'chatterbot.logic.LowConfidenceAdapter',
	],
	input_adapter='chatterbot.input.TerminalAdapter',
	output_adapter='chatterbot.output.TerminalAdapter',
	database='../database.sqlite3',
)
bot.set_trainer(ListTrainer)
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train('chatterbot.corpus.english')
bot.logger.info('Trained database generated succesfully!')
print('Hello, I am Joshua. And you are...?')


# The following loop will execute each time the user enters input
while True:
	try:

    	#chatterbot
		# We pass None to this method because the parameter
        # is not used by the TerminalAdapter
		bot_input = bot.get_response(None)
# Press ctrl-c or ctrl-d on the keyboard to exit
	except(KeyboardInterrupt, EOFError, SystemExit):
		break
