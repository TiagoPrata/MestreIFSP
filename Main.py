# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

helpTxt = """Olá, {},

Veja abaixo a lista de comandos que pode usar para interagir comigo:
/IMMDT -  Para obter visualizar as orientações dadas pelo professor Flávio;

Por enquanto é só, mas em breve suportarei mais comandos para te ajudar. :)"""

immdtImagePath="images/IMMDT/orientacoes.png"
		  
unknownTxt = "Desculpe, porém eu não conheço esse comando.\nDigite /help ou /h para conhecer os comandos que pode utilizar comigo."

def start(bot, update):
    update.message.reply_text('Olá, sou o MestreIFSP e vou tentar te ajudar com questões do Mestrado no IFSP-SP.\n\nDigite /help ou /h para conhecer os comandos em que eu posso te ajudar.')
	
def help(bot, update):
    update.message.reply_text(
        helpTxt.format(update.message.from_user.first_name))
		
def h(bot, update):
    update.message.reply_text(
        helpTxt.format(update.message.from_user.first_name))

def IMMDT(bot, update):	
	bot.send_photo(chat_id=update.message.chat_id, photo=open(immdtImagePath, 'rb'))
	bot.send_message(chat_id=update.message.chat_id, text="Para cadastro no POSGERE o link é:\nhttp://seer.spo.ifsp.edu.br/index.php/posgere/user/register")

def unknown(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=unknownTxt)

updater = Updater('397179894:AAE0Cq2sRmZH7YVz7p-OdqXPS-4wHj5vq4M')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('h', h))
updater.dispatcher.add_handler(CommandHandler('IMMDT', IMMDT))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
updater.idle()
