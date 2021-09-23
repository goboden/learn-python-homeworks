def is_valid_symbol(symbol: str):
    valid_symbols = '1234567890+-*/()'
    return symbol in valid_symbols


def text_to_expression(text):
    expression = [x for x in text if is_valid_symbol(x)]
    return ''.join(expression)


def reply(context, user_id, user_text: str):
    expression_text = text_to_expression(user_text)
    try:
        result = eval(expression_text)
        return f'{expression_text} = {result}'
    except ZeroDivisionError:
        return f'Ошибка. Деление на 0. {expression_text}'
