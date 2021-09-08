
def hello_user():
    while True:
        user_input = input('Как дела? ')
        if user_input.upper() == 'ХОРОШО':
            break


hello_user()
