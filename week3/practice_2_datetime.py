from datetime import datetime, timedelta
import locale


def main():
    dt_now = datetime.now()
    dt_yesterday = dt_now - timedelta(days=1)
    dt_30_days_ago = dt_now - timedelta(days=30)

    locale.setlocale(locale.LC_TIME, 'russian')
    print('Вчера: {}'.format(dt_yesterday.strftime('%d %B %Y')))
    print('Сегодня: {}'.format(dt_now.strftime('%d %B %Y')))
    print('30 дней назад: {}'.format(dt_30_days_ago.strftime('%d %B %Y')))

    date_string = '01/01/25 12:10:03.234567'
    dt_from_string = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print('Дата {}, тип {}'.format(dt_from_string, type(dt_from_string)))


if __name__ == '__main__':
    main()
