import telebot
from telebot import types

# Твой токен
TOKEN = "8018020965:AAFVqwp12JL8mRMT-Mcpg2on2zAh5wW0QaM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📍 Магазины рядом")
    btn2 = types.KeyboardButton("🕘 Часы работы")
    btn3 = types.KeyboardButton("🎯 Акции и скидки")
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(
        message.chat.id, 
        "Привет! Выбери, что тебя интересует 👇", 
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📍 Магазины рядом":
        bot.send_message(message.chat.id, "Вот список ближайших магазинов в Батуми 🏪")
    elif message.text == "🕘 Часы работы":
        bot.send_message(message.chat.id, "Обычные часы работы: с 09:00 до 18:00 🕔")
    elif message.text == "🎯 Акции и скидки":
        bot.send_message(message.chat.id, "Сейчас действуют следующие акции: ... 🎁")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выбери одну из кнопок ⬇️")

print("Бот запущен. Ожидаю команды...")

bot.polling()
