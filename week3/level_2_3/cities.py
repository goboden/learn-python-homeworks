import json


cities_db = dict()


class TooManyWords(Exception):
    pass


class CityNotFound(Exception):
    pass


def valid_city_name(word: str):
    if word.isalpha():
        city_name = word.upper()
        cities_list = cities_db.get(city_name[0], [])
        if city_name in cities_list:
            return city_name
        else:
            raise CityNotFound
    raise ValueError


def validate_user_input(user_text: str):
    words = user_text.split()
    if len(words) > 1:
        raise TooManyWords
    city_name = valid_city_name(words[0])
    return city_name


def reply(context, user_id: str, user_text: str):
    try:
        valid_city_name = validate_user_input(user_text)
        return valid_city_name
    except TooManyWords:
        return 'Введите одно слово'
    except CityNotFound:
        return 'Город не найден в базе'


def load_cities_db():
    with open('cities.json', 'r', encoding='utf-8') as f:
        return json.load(f)


cities_db = load_cities_db()
