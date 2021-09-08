
ls = [3, 5, 7, 9, 10.5]
print(ls)
ls.append('Python')
print(len(ls))

print(ls[0])
print(ls[-1])
print(ls[1:4])

ls.remove('Python')
print(ls)

dt = {'city': 'Москва', 'temperature': '20'}
print(dt['city'])

temp = dt['temperature']
temp = int(temp) - 5
dt['temperature'] = str(temp)
print(dt)


if 'country' in dt:
    print('Ключ "country" есть')
else:
    print('Ключа "country" нет')

country = dt.get('country', 'Россия')
print(country)

dt['date'] = '27.05.2019'
print(dt)
print(len(dt))
