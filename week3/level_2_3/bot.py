import telegram
from telegram.ext import Updater, CommandHandler
import logging
import settings
import wordcount
import next_full
import cities
import calc

logging.basicConfig(filename='bot.log', level=logging.INFO)
bot_commands = {
    'wordcount': wordcount,
    'next_full_moon': next_full,
    'cities': cities,
    'calc': calc,
}


def validate_user_text(user_text: str):
    words = user_text.split()
    return '' if len(words) < 2 else ' '.join(words[1:])


def get_command_handler(command: str):
    command_module = bot_commands[command]

    def command_handler(update: telegram.update.Update, context):
        user_id = update.message.from_user.id
        user_text = validate_user_text(update.message.text)
        reply_text = command_module.reply(context, user_id, user_text)
        if reply_text:
            update.message.reply_text(reply_text)

    return command_handler


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    for command in bot_commands:
        dp.add_handler(CommandHandler(command, get_command_handler(command)))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
