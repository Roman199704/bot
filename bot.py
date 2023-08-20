import telebot
from telebot import types

bot = telebot.TeleBot('6365110095:AAGzwoVDAr2i6Xr8Yt_vx6KTC6eERctPPMI')

@bot.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь расскажу немного о нашей компании?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
  markup.add(button_yes)
  bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True) #обязательная для работы бота часть