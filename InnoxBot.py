# Install python-telegram-bot
# $ pip install python-telegram-bot
# $ pip install python-telegram-bot --upgrade
# $ git clone https://github.com/python-telegram-bot/python-telegram-bot
# $ cd python-telegram-bot
# $ python setup.py install


#from telegram import Updater
import telegram


menu_keyboard = telegram.ReplyKeyboardMarkup(['/start','/menu','/help'])
menu_keyboard.one_time_keyboard=False
menu_keyboard.resize_keyboard=True

def start(bot, update):
	bot.sendMessage(update.message.chat_id, text='Hi! I am manuele ')
	menu(bot, update)

def menu(bot, update):
	bot.sendMessage(update.message.chat_id, text="Seleziona un comando dalla tastiera qui sotto", reply_markup=menu_keyboard)

def main():
	# Create the EventHandler and pass it your bot's token.
	updater = telegram.Updater(token="XXXX")

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.addTelegramCommandHandler("start", start)
	dp.addTelegramCommandHandler("menu", menu)

	# Start the Bot
	updater.start_polling()

	updater.idle()

if __name__ == '__main__':
	main()
