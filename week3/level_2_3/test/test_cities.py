import cities
import pytest


class TelegramContextMock():
    def __init__(self):
        self.user_data = dict()


def test_valid_city_name():
    assert cities.valid_city_name('сАрАтОв') == 'САРАТОВ'
    assert pytest.raises(ValueError, cities.valid_city_name, 'сАрАтОв1')


def test_validate_user_input():
    context = TelegramContextMock()
    user_data = context.user_data
    assert pytest.raises(cities.CityNotFound, cities.validate_user_input,
                         'сАрАтОвВ', user_data)


def test_reply():
    context = TelegramContextMock()
    assert cities.reply(context, None,
                        '1 2 3') == 'Введено больше одного слова.'
    assert cities.reply(context, None, 'Москва') == 'Аша'


@pytest.mark.usertest
def test_telegram_context():
    context = TelegramContextMock()

    reply = cities.reply(context, None, 'Москва1')
    assert reply == 'Название должно содержать только буквы.'

    reply = cities.reply(context, None, 'Москва')
    assert reply == 'Аша'
    assert context.user_data['last_city'] == 'АША'

    reply = cities.reply(context, None, 'Аша')
    assert reply == 'Этот город уже был.'

    reply = cities.reply(context, None, 'Королев')
    assert reply == 'Город должен начинаться на букву А.'

    reply = cities.reply(context, None, 'Аша')
    assert reply == 'Этот город уже был.'

    assert 'АНАПА' in context.user_data['cities']['А']

    reply = cities.reply(context, None, 'Анапа')
    assert reply == 'Анадырь'

    assert 'АНАПА' in context.user_data['drop']
    assert 'АНАПА' not in context.user_data['cities']['А']

    context = TelegramContextMock()
    reply = cities.reply(context, None, 'Москва')
    assert reply == 'Аша'