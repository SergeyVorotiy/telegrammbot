import telebot
from config import BOT_TOKEN, VALUES
from exceptions import Price

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'help', ])
def start_bot(message):
    text = f'{message.chat.username}, Для начала работы c бота введите команду в формате: \n' \
           f'<Название валюты для перевода> <Название валюты, в которую переводить> <количество первой валюты>\n' \
           f'информация о доступных валютах для конвертации доступна по команде: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values', ])
def send_value(message):
    text = ''
    for key in VALUES.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, f"Доступные валюты:{text}")

@bot.message_handler(content_types=['text', ])
def convert(message):
    m = message.text.split(' ')
    result = Price.get_price(m)
    bot.send_message(message.chat.id, result)

bot.polling()