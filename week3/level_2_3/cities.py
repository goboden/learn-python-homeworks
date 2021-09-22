import json
import copy


cities_db = dict()


class CityGameException(Exception):
    pass


class TooManyWords(CityGameException):
    def __init__(self):
        self.text = 'Введено больше одного слова.'


class CityNotFound(CityGameException):
    def __init__(self):
        self.text = 'Такого города нет.'


class NoMoreCities(CityGameException):
    def __init__(self):
        self.text = 'Я проиграл. Начинаем сначала.'


class WrongFirstLetter(CityGameException):
    def __init__(self, letter):
        self.text = f'Город должен начинаться на букву {letter}.'


class CityRepeat(CityGameException):
    def __init__(self):
        self.text = 'Этот город уже был.'


def valid_city_name(word: str):
    if word.isalpha():
        city_name = word.upper()
        cities_list = cities_db.get(city_name[0], [])
        if city_name in cities_list:
            return city_name
        else:
            raise CityNotFound
    raise ValueError


def validate_user_input(user_text: str, user_data: dict):
    words = user_text.split()
    if len(words) > 1:
        raise TooManyWords
    city_name = valid_city_name(words[0])

    last_city = user_data['last_city']
    if last_city and last_city[-1] != city_name[0]:
        raise WrongFirstLetter(last_city[-1])

    drop = user_data['drop']
    if city_name in drop:
        raise CityRepeat
    else:
        drop.add(city_name)

    return city_name


def user_data_from_context(context):
    cities = context.user_data.get('cities', copy.deepcopy(cities_db))
    drop = context.user_data.get('drop', set())
    last_city = context.user_data.get('last_city', None)
    return {'cities': cities, 'drop': drop, 'last_city': last_city}


def user_data_to_context(user_data, context):
    context.user_data['cities'] = user_data['cities']
    context.user_data['drop'] = user_data['drop']
    context.user_data['last_city'] = user_data['last_city']


def find_next_city(city_name: str, user_data: dict):
    cities = user_data['cities']
    drop = user_data['drop']
    cities_by_letter = cities[city_name[0]]
    cities_by_letter.remove(city_name)

    cities_by_letter = cities.get(city_name[-1], [])
    if len(cities_by_letter) == 0:
        raise NoMoreCities
    else:
        next_city = cities_by_letter[0]
        cities_by_letter.remove(next_city)
        drop.add(next_city)
        user_data['last_city'] = next_city
        return next_city


def reply(context, user_id: str, user_text: str):
    try:
        user_data = user_data_from_context(context)
        valid_city_name = validate_user_input(user_text, user_data)
        next_city = find_next_city(valid_city_name, user_data)
        user_data_to_context(user_data, context)
        return next_city.capitalize()
    except (CityGameException) as ex:
        return ex.text
    except ValueError:
        return 'Название должно содержать только буквы.'


def load_cities_db():
    with open('cities.json', 'r', encoding='utf-8') as f:
        return json.load(f)


cities_db = load_cities_db()
