
def two_strings(string_one, string_two):
    if isinstance(string_one, str) and isinstance(string_two, str):
        if string_one == string_two:
            return 1
        elif string_two == 'learn':
            return 3
        elif len(string_one) > len(string_two):
            return 2
    else:
        return 0


def test(a, b):
    res = two_strings(a, b)
    print('Строка1 = {}, Строка2 = {}, Результат = {}'.format(a, b, res))


if __name__ == '__main__':
    test(1, 2)
    test('learn', 2)
    test('learn', 'learn')
    test('learn', 'lear')
    test('lear1', 'learn')
    test('learn', 'lear1')
