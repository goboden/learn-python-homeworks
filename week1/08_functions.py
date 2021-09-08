
def get_summ(one, two, delimiter='&'):
    return delimiter.join((str(one), str(two))).upper()


print(get_summ('Learn', 'python'))
