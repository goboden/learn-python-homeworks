
def occupation(age):
    age = int(age)
    if age < 0 or age > 100:  # Например 100
        raise ValueError
    if age < 7:
        return 'учеба в детском саду'
    elif age < 17:
        return 'учеба в школе'
    elif age < 22:
        return 'учеба в ВУЗе'
    else:
        return 'работа'


def main():
    age = input('Укажите возраст: ')
    try:
        ocp = occupation(age)
        print('Возраст: {}. Занятие: {}'.format(age, ocp))
    except ValueError:
        print('Возраст указан неверно')


if __name__ == '__main__':
    main()
