from telegram import Updater


def start(bot, update):
	bot.sendMessage(update.message.chat_id, text='Hi! I am manuele ')

def main():
	# Create the EventHandler and pass it your bot's token.
	updater = Updater(token="XXXX")

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.addTelegramCommandHandler("start", start)

	# Start the Bot
	updater.start_polling()

	updater.idle()

if __name__ == '__main__':
	main()
