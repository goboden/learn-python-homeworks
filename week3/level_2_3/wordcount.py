def word_representation(words_count):
    repr = 'слов'
    if words_count == 0:
        repr = 'слов'
    elif words_count % 100 >= 10 and words_count % 100 <= 20:
        repr = 'слов'
    elif words_count % 10 == 1:
        repr = 'слово'
    elif words_count % 10 >= 2 and words_count % 10 <= 4:
        repr = 'слова'
    return repr


def words_are_valid(words: list[str]):
    for word in words:
        if not word.isalpha():
            return False
    return True


def reply(context, user_id, user_text: str):
    words = user_text.split()
    if words_are_valid(words):
        words_count = len(words)
        words_repr = word_representation(words_count)
        return f'{words_count} {words_repr}'
    else:
        return 'Слова некорректные'


if __name__ == '__main__':
    for words_count in range(200):
        words_repr = word_representation(words_count)
        print(f'{words_count} {words_repr}')
