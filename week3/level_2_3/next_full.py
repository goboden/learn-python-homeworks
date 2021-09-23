import ephem
from datetime import datetime


class DateParseError(Exception):
    pass


def date_from_user_text(user_text: str):
    try:
        if user_text == '' or user_text.isspace():
            return datetime.now()
        else:
            return datetime.strptime(user_text, '%d-%m-%Y')
    except ValueError:
        raise DateParseError


def reply(context, user_id, user_text: str):
    try:
        user_date = date_from_user_text(user_text)
        full_moon_date = ephem.next_full_moon(user_date)
        date_str = datetime.strftime(full_moon_date.datetime(), '%d-%m-%Y')
        return f'Ближайшее полнолуние {date_str}'
    except DateParseError:
        return 'Дата не соответствует формату День-Месяц-Год (25-03-2021)'
