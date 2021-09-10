from telegram.ext import Updater, CommandHandler
import ephem
import logging
import settings


logging.basicConfig(filename='bot.log', level=logging.INFO)
planets = [name for _1, _2, name in ephem._libastro.builtin_planets()]


def constellation(planet_name):
    if planet_name == '':
        return 'Укажите имя планеты на английском'
    elif planet_name in planets:
        Planet = getattr(ephem, planet_name)
        planet = Planet(ephem.now())
        constellation = ephem.constellation(planet)
        return f'Планета {planet_name} находится в {constellation[1]}'
    else:
        return f'Планета {planet_name} не найдена'


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def planet_constellation(update, context):
    words = update.message.text.split()
    planet_name = words[1] if len(words) > 1 else ''
    update.message.reply_text(constellation(planet_name))


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_constellation))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
