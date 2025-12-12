import telebot
import os
import sys
import traceback
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

ADMIN_ID = 7366680681


from password_manager import Password
password_manager = Password()


@bot.message_handler(commands=['restart'])
def restart_bot(message):
    if message.from_user.id == ADMIN_ID:
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        bot.send_message(message.chat.id, "у вас нет прав на эту команду")


@bot.message_handler(commands=['generate'])
def generate_command(message):
    parts = message.text.split()
    if len(parts) > 1:
        try:
            length = int(parts[1])
        except ValueError:
            bot.send_message(message.chat.id, "Пожалуйста, укажите число для длины пароля")
            return
    else:
        length = 12

    password = password_manager.generation_password(string_length=length)
    password_manager.password_storage.append(password)


    # password_manager.password_storage(count=1, length=length)

    bot.send_message(message.chat.id, f"Ваш сгенерированный пароль:\n{password}")


@bot.message_handler(commands=['passwords'])
def password_command(message):

    passwords = password_manager.get_storage()

    if passwords:
        password_text = "\n".join([f"{i+1}. {pwd}" for i, pwd in enumerate(passwords)])
        bot.send_message(message.chat.id, f"Ваши пароли:\n{password_text}")
    else:
        bot.send_message(message.chat.id, "У вас еще нет сохраненных паролей")


@bot.message_handler(commands=['clear'])
def clear_command(message):
    password_manager.clear_storage()
    bot.send_message(message.chat.id, "Все пароли удалены")

@bot.message_handler(commands=['admin'])
def admin_command(message):
    bot.send_message(message.chat.id, "угрозы сюда: @wrbtf")



@bot.message_handler(commands=['start'])
def start_command(message):
    help_text = """Команды:
/generate [длина] - создать пароль (по умолчанию 12 символов)
/passwords - показать все сохраненные пароли
/clear - удалить все пароли
/admin
"""

    bot.send_message(message.chat.id, help_text)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)