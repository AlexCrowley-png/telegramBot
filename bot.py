import telebot

bot = telebot.TeleBot('1294332349:AAEHx03qZ0NlwaxnCnj7A3Q0pF1V9640NDA')
chat_base =[]
is_hi = []


@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привет, Браток, твой /start был услышан, скоро с тобой свяжется специально обученая Дура! Можешь с ней поздороваться)')

@bot.message_handler(content_types = ['text'])

def send_message(message):
    if ("дура" in message.text.lower()):
        bot.send_message(message.chat.id,  "Сам дурак!")
    elif ("привет" in message.text.lower()):
        if (not message.chat.id in chat_base):
            chat_base.append(message.chat.id)
            is_hi.append(False)
        if is_hi[chat_base.index(message.chat.id)] != True:
            is_hi[chat_base.index(message.chat.id)] = True
            bot.send_message(message.chat.id, "Привет! как жизнь, как дела?")
        else:
            bot.send_message(message.chat.id, "Ты что, дурак? мы уже поздоровались!")

    elif ("пока" in message.text.lower()):
        if (not message.chat.id in chat_base):
            chat_base.append(message.chat.id)
            is_hi.append(False)
        if is_hi[chat_base.index(message.chat.id)]:
            is_hi[chat_base.index(message.chat.id)] = False
            bot.send_message(message.chat.id, "Пока. Ты это, заходи, если что!")
        else:
            bot.send_message(message.chat.id, "Мы еще не поздоровались, а ты уже прощаешься!")
    elif ("барнаул" in message.text.lower()):
        bot.send_message(message.chat.id,  "Прости, я не знаю ничего про Барнаул... Но я знаю кто может в этом помочь!!! \nОбратись к https://t.me/GetWeatherTestBot")
    elif ("пиво" in message.text.lower()):
        bot.send_message(message.chat.id, "Пиво!!?!")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMEX52r4DRWfPUUBXaP2uboo8iJt34AAg0AA4lAqw3avUV4gA25yRsE")
    else:
        bot.send_message(message.chat.id,  "Истинный человек не написал бы: \"" + message.text + "\"\nОн написал бы: \"Сам дурак, пшел нахрен!\"")
    print(message.chat.username + " написал: " + message.text)


bot.polling()
