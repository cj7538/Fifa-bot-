import telebot

TOKEN = "8352010148:AAG7aFvIFZSeyh4Z-1G1tQ8e9ppo_AaF4EM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenue ! Bot FIFA actif ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Tu as dit : {message.text}")

bot.polling()
