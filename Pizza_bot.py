import telebot
from handler_message import Handler_message
import Config

bot = telebot.TeleBot(Config.TOKEN)
handler = Handler_message()

@bot.message_handler()

def send_answer(message):
    bot.send_message(
        message.chat.id,
        handler.get_answer(message.chat.id, message.text)
    )


if __name__ == '__main__':
    bot.polling(none_stop=True)