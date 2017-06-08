# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import random
import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

shutdownPassword="abc1234"

helpTxt = """Olá, {},

Veja abaixo a lista de comandos que pode usar para interagir comigo:
/IMMDT -  Para obter visualizar as orientações dadas pelo professor Flávio;

Por enquanto é só, mas em breve suportarei mais comandos para te ajudar. :)"""

immdtImagePath="images/IMMDT/orientacoes.png"

shutdownTxt="Estou indo dormir... Ate logo!"

unknownTxt = "Desculpe, porém eu não conheço esse comando.\nDigite /help ou /h para conhecer os comandos que pode utilizar comigo."

t0 = [  'Caros amigos, ',
	'Por outro lado, ',
	'Assim mesmo, ',
	'No entanto, não podemos esquecer que ',
	'Do mesmo modo, ',
	'A prática cotidiana prova que ',
	'Nunca é demais lembrar o peso e o significado destes problemas, uma vez que ',
	'As experiências acumuladas demonstram que ',
	'Acima de tudo, é fundamental ressaltar que ',
	'O incentivo ao avanço tecnológico, assim como ',
	'Não obstante, ',
	'Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se ',
	'Pensando mais a longo prazo, ',
	'O que temos que ter sempre em mente é que ',
	'Ainda assim, existem dúvidas a respeito de como ',
	'Gostaria de enfatizar que ',
	'Todavia, ',
	'A nível organizacional, ',
	'O empenho em analisar ',
	'Percebemos, cada vez mais, que ',
	'No mundo atual, ',
	'É importante questionar o quanto ',
	'Neste sentido, ',
	'Evidentemente, ',
	'Por conseguinte, ',
	'É claro que ',
	'Podemos já vislumbrar o modo pelo qual ',
	'Desta maneira, ',
	'O cuidado em identificar pontos críticos n',
	'A certificação de metodologias que nos auxiliam a lidar com ' ]

t1 = [	'a execução dos pontos do programa ',
	'a complexidade dos estudos efetuados ',
	'a contínua expansão de nossa atividade ',
	'a estrutura atual da organização ',
	'o novo modelo estrutural aqui preconizado ',
	'o desenvolvimento contínuo de distintas formas de atuação ',
	'a constante divulgação das informações ',
	'a consolidação das estruturas ',
	'a consulta aos diversos militantes ',
	'o início da atividade geral de formação de atitudes ',
	'o desafiador cenário globalizado ',
	'a mobilidade dos capitais internacionais ',
	'o fenômeno da Internet ',
	'a hegemonia do ambiente político ',
	'a expansão dos mercados mundiais ',
	'o aumento do diálogo entre os diferentes setores produtivos ',
	'a crescente influência da mídia ',
	'a necessidade de renovação processual ',
	'a competitividade nas transações comerciais ',
	'o surgimento do comércio virtual ',
	'a revolução dos costumes ',
	'o acompanhamento das preferências de consumo ',
	'o comprometimento entre as equipes ',
	'a determinação clara de objetivos ',
	'a adoção de políticas descentralizadoras ',
	'a valorização de fatores subjetivos ',
	'a percepção das dificuldades ',
	'o entendimento das metas propostas ',
	'o consenso sobre a necessidade de qualificação ',
	'o julgamento imparcial das eventualidades ' ]

t2 = [  'nos obriga à análise ',
	'cumpre um papel essencial na formulação ',
	'exige a precisão e a definição ',
	'auxilia a preparação e a composição ',
	'garante a contribuição de um grupo importante na determinação ',
	'assume importantes posições no estabelecimento ',
	'facilita a criação ',
	'obstaculiza a apreciação da importância ',
	'oferece uma interessante oportunidade para verificação ',
	'acarreta um processo de reformulação e modernização ',
	'pode nos levar a considerar a reestruturação ',
	'representa uma abertura para a melhoria ',
	'ainda não demonstrou convincentemente que vai participar na mudança ',
	'talvez venha a ressaltar a relatividade ',
	'prepara-nos para enfrentar situações atípicas decorrentes ',
	'maximiza as possibilidades por conta ',
	'desafia a capacidade de equalização ',
	'agrega valor ao estabelecimento ',
	'é uma das consequências ',
	'promove a alavancagem ',
	'não pode mais se dissociar ',
	'possibilita uma melhor visão global ',
	'estimula a padronização ',
	'aponta para a melhoria ',
	'faz parte de um processo de gerenciamento ',
	'causa impacto indireto na reavaliação ',
	'apresenta tendências no sentido de aprovar a manutenção ',
	'estende o alcance e a importância ',
	'deve passar por modificações independentemente ',
	'afeta positivamente a correta previsão ' ]


t3 = [  'das condições financeiras e administrativas exigidas.',
	'das diretrizes de desenvolvimento para o futuro.',
	'do sistema de participação geral.',
	'das posturas dos órgãos dirigentes com relação às suas atribuições.',
	'das novas proposições.',
	'das direções preferenciais no sentido do progresso.',
	'do sistema de formação de quadros que corresponde às necessidades.',
	'das condições inegavelmente apropriadas.',
	'dos índices pretendidos.',
	'das formas de ação.',
	'dos paradigmas corporativos.',
	'dos relacionamentos verticais entre as hierarquias.',
	'do processo de comunicação como um todo.',
	'dos métodos utilizados na avaliação de resultados.',
	'de todos os recursos funcionais envolvidos.',
	'dos níveis de motivação departamental.',
	'da gestão inovadora da qual fazemos parte.',
	'dos modos de operação convencionais.',
	'de alternativas às soluções ortodoxas.',
	'dos procedimentos normalmente adotados.',
	'dos conhecimentos estratégicos para atingir a excelência.',
	'do fluxo de informações.',
	'do levantamento das variáveis envolvidas.',
	'das diversas correntes de pensamento.',
	'do impacto na agilidade decisória.',
	'das regras de conduta normativas.',
	'do orçamento setorial.',
	'do retorno esperado a longo prazo.',
	'do investimento em reciclagem técnica.',
	'do remanejamento dos quadros funcionais.' ]

def sayit():
	return random.choice(t0)+random.choice(t1)+random.choice(t2)+random.choice(t3)

def start(bot, update):
    update.message.reply_text('Olá, sou o MestreIFSP e vou tentar te ajudar com questões do Mestrado no IFSP-SP.\n\nDigite /help ou /h para conhecer os comandos em que eu posso te ajudar.')

def shutdown(bot, update, args):
    if len(args) > 0:
        if args[0]==shutdownPassword:
            bot.send_message(chat_id=update.message.chat_id, text=shutdownTxt)
            sys.exit()

def lerolero(bot, update):
    update.message.reply_text(sayit())

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
updater.dispatcher.add_handler(CommandHandler('shutdown', shutdown, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('lerolero', lerolero))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('h', h))
updater.dispatcher.add_handler(CommandHandler('IMMDT', IMMDT))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
updater.idle()
