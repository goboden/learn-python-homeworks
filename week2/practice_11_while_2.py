
quest = {
    'Как дела?': 'Хорошо!',
    'Что делаешь?': 'Программирую'
}


def ask_user():
    user_input = input('Введите вопрос: ')
    if user_input in quest:
        print(quest[user_input])
        return True
    return False


while ask_user():
    pass
