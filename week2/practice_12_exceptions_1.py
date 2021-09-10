
def hello_user():
    while True:
        try:
            user_input = input('Как дела? ')
            if user_input.upper() == 'ХОРОШО':
                break
        except KeyboardInterrupt:
            print('Пока!')
            break


hello_user()
