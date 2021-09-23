import calc


def test_text_to_expression():
    expression = calc.text_to_expression('1 + 2+  3 /5*10 ')
    assert expression == '1+2+3/5*10'


def test_reply():
    reply = calc.reply(None, None, '1   +   2+3   / 5   * 1    0   ')
    assert reply == '1+2+3/5*10 = 9.0'
    reply = calc.reply(None, None, '(1asd+asd2+3/5*asdasd10) / 0')
    assert reply == 'Ошибка. Деление на 0. (1+2+3/5*10)/0'
