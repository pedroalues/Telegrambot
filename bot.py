import telebot

CHAVE_API = "5765399984:AAF8vjW3cRrvx2JrsNZGxh9sq06gKOxA9qc"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
     bot.send_message(mensagem.chat.id, "saindo a pizza para sua casa: tempo de espera em 20min")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
     bot.send_message(mensagem.chat.id, "saindo o brabo:em 10 min chega ai")

@bot.message_handler(commands=["salada"])
def salada(mensagem):
     bot.send_message(mensagem.chat.id, "nao tem salada nao, clique aqui para iniciar: /iniciar")


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """ 
    O que voce quer? (clique em uma opcao)
    /pizza Pizza
    /hamburguer Hamburguer
    /salada Salada"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "para enviar uma reclamacao, mande um email para reclamacao@gmail,br")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.reply_to(mensagem.chat.id, "Valeu, Salve!!!")


def verificar(mensagem):
        return True
  

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
        /opcao1 fazer um pedido
        /opcao2 reclamar de um pedido
        /opcao3 mandar um salve
     Responder qaulquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)


bot.polling()
