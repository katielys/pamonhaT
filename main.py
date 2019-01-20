from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re
listaOI = ["oi",'Ola']
listaCIAO = ['tchau','Bye','Tchau']
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
    bot.send_message(chat_id=chat_id,text="Nao tem nada util ainda \nDale o comando :/auau\nHey "+update.message.from_user.first_name + " <3")

def echo(bot,update):
    if((update.message.text not in listaCIAO)):
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    else :
        bot.send_message(chat_id=update.message.chat_id, text="Tchau\n\n Ate a proxima! \n ")   

def main():
    updater = Updater('722473469:AAGkohZwDu86zEwW4Wfj8j7JRxTAIg_oEl4')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('auau',bop))
    dp.add_handler(CommandHandler('start',sendTexto))
    echo_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
