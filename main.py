from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
token = 'AAGkohZwDu86zEwW4Wfj8j7JRxTAIg_oEl4'
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def sendTexto(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="Dale o comando :/auau")
def main():
    updater = Updater('722473469:AAGkohZwDu86zEwW4Wfj8j7JRxTAIg_oEl4')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('auau',bop))
    dp.add_handler(CommandHandler('start',sendTexto))
    ##updaterreply_text("Ta no inicio, calma ai ")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
