
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        referat_text = f.read()
        return referat_text


def write_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def main():
    referat = read_file('referat.txt')
    words = referat.split()
    print(f'Длинна файла: {len(referat)}')
    print(f'Количество слов: {len(words)}')

    referat2 = referat.replace('.', '!')
    write_file('referat2.txt', referat2)


if __name__ == '__main__':
    main()
