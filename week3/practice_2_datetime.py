from datetime import datetime, timedelta
import locale


def print_days():
    dt_now = datetime.now()
    dt_yesterday = dt_now - timedelta(days=1)
    dt_30_days_ago = dt_now - timedelta(days=30)

    locale.setlocale(locale.LC_TIME, 'russian')
    print('Вчера: {}'.format(dt_yesterday.strftime('%d %B %Y')))
    print('Сегодня: {}'.format(dt_now.strftime('%d %B %Y')))
    print('30 дней назад: {}'.format(dt_30_days_ago.strftime('%d %B %Y')))


def str_2_datetime(date_string):
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')


if __name__ == '__main__':
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
