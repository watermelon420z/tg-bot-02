import os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# token = "5634251411:AAF94qW8CkVgi_h4r3w_R5h4H-..."
token = os.environ.get('TG_BOT_TOKEN') # пж пять поставьте за это


def echo(update, context):
    text = update.message.text
    if text.lower() in ['привет', 'приветик']:
        text = "привет кент!"

    update.message.reply_text(f"{text}")


def help(update, context):
    update.message.reply_text("Список доступных команд \n • /help - вывод помощи")


def start(update, context):
    update.message.reply_text("привет! \n набери /help, чтобы поглазеть на список команд")


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен")

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
