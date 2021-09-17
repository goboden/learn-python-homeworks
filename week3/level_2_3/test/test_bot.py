import bot
import cities
import types
import pytest


def test_user_message_parse():
    user_text = bot.validate_user_text('/command test message')
    assert user_text == 'test message', user_text

    user_text = bot.validate_user_text('/command     test     message')
    assert user_text == 'test message', user_text

    user_text = bot.validate_user_text('/command          ')
    assert user_text == '', user_text


def test_get_command_handler():

    def has_handler(command):
        module = bot.bot_commands[command]
        foo = getattr(module, 'reply')
        assert isinstance(foo, types.FunctionType)

    has_handler('wordcount')
    has_handler('next_full_moon')
    has_handler('cities')
    has_handler('calc')


def test_word_count():
    module = bot.bot_commands['wordcount']
    assert module.reply(None, None, 'Слово1 Слово2') == 'Слова некорректные'
    assert module.reply(None, None, 'Слово Слово') == '2 слова'


def test_next_full_moon():
    module = bot.bot_commands['next_full_moon']
    reply = module.reply(None, None, '21-03-2021')
    assert reply == 'Ближайшее полнолуние 28-03-2021'

    reply = module.reply(None, None, '')
    assert reply == 'Ближайшее полнолуние 20-09-2021'

    reply = module.reply(None, None, '     ')
    assert reply == 'Ближайшее полнолуние 20-09-2021'

    reply = module.reply(None, None, '21-03-21')
    assert reply == 'Дата не соответствует формату День-Месяц-Год (25-03-2021)'


def test_cities():
    assert cities.valid_city_name('сАрАтОв') == 'САРАТОВ'

    assert pytest.raises(ValueError, cities.valid_city_name, '1')

    assert pytest.raises(cities.CityNotFound,
                         cities.validate_user_input,
                         'сАрАтОвВ')

    module = bot.bot_commands['cities']
    reply = module.reply(None, None, '1 2 3')
    assert reply == 'Введите одно слово'

    reply = module.reply(None, None, 'Москва')
    assert reply == 'МОСКВА'
