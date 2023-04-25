import telebot
import random
import string

# Set up Telegram bot token
bot_token = 'Your Telegram Bot API'
bot = telebot.TeleBot(bot_token)

# Define password generating function
def generate_password(length, word):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(length - len(word))) + word
    password = ''.join(random.sample(password, len(password)))
    return password


# Define start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Password Generator Bot!\nSend me the length of the password you want to generate.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "I support the following commands: \n /start  : Starts the bot \n /info   : Get info about the bot \n /help   : Self Explainatory \n /status  : To check the status of the bot")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "I am a simple Password Generator Telegram bot.")

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "I am up and running.")


# Define password generation command handler
@bot.message_handler(func=lambda message: True)
def generate_password_command(message):
    try:
        password_length, *password_word = message.text.split()
        password_length = int(password_length)
        if password_word:
            password_word = password_word[0]
            password = generate_password(password_length, password_word)
            bot.reply_to(message, f"Here's your new password: {password}")
        else:
            password = generate_password(password_length, "")
            bot.reply_to(message, f"Here's your new password:\n{password}")
    except ValueError:
        bot.reply_to(message, "Please send me a valid integer for the password length.")

# Start the bot
bot.polling()
