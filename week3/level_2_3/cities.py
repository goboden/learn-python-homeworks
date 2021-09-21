import json
import copy


cities_db = dict()


class TooManyWords(Exception):
    def __init__(self):
        self.text = 'Введено больше одного слова'


class CityNotFound(Exception):
    def __init__(self):
        self.text = 'Такого города нет'


class NoMoreCities(Exception):
    def __init__(self):
        self.text = 'Я проиграл. Начинаем сначала.'


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


def user_data(context):
    cities = context.user_data.get('cities', copy.deepcopy(cities_db))
    drop = context.user_data.get('drop', set())
    last_city = context.user_data.get('last_city', None)
    return cities, drop, last_city


def find_next_city(city_name: str, cities: dict, drop: set):
    cities_by_letter = cities[city_name[0]]
    cities_by_letter.remove(city_name)

    cities_by_letter = cities.get(city_name[-1], [])
    if len(cities_by_letter) == 0:
        raise NoMoreCities
    else:
        next_city = cities_by_letter[0]
        drop.add(next_city)
        cities_by_letter.remove(next_city)
        return next_city


def reply(context, user_id: str, user_text: str):
    try:
        valid_city_name = validate_user_input(user_text)
        user_cities, user_drop, last_city = user_data(context)
        if last_city and last_city[-1] != valid_city_name[0]:
            return f'Город должен начинаться на букву {last_city[-1]}'
        if valid_city_name in user_drop:
            return 'Этот город уже был'
        else:
            user_drop.add(valid_city_name)
        next_city = find_next_city(valid_city_name, user_cities, user_drop)

        context.user_data['cities'] = user_cities
        context.user_data['drop'] = user_drop
        context.user_data['last_city'] = next_city
        return next_city.capitalize()
    except (TooManyWords, CityNotFound, NoMoreCities) as ex:
        return ex.text
    except ValueError:
        return 'Название должно содержать только буквы'


def load_cities_db():
    with open('cities.json', 'r', encoding='utf-8') as f:
        return json.load(f)


cities_db = load_cities_db()
