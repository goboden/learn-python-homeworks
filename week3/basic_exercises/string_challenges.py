# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print('----------')


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.upper().count('А'))
print('----------')


# Вывести количество гласных букв в слове
word = 'Архангельскeee'
letters = 'АОУЫЭЯЕЮИ'
count = [letter for letter in word.upper() if letter in letters]
print(len(count))
print('----------')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
print('----------')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])
print('----------')


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
averages = [len(word) for word in sentence.split()]
print(round(sum(averages) / len(averages), 2))
print('----------')
