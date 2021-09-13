from collections import Counter

# Задание 1
# Дан список учеников,
# нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


def student_names_counter(students):
    names = [dct['first_name'] for dct in students]
    return Counter(names)


names_counter = student_names_counter(students)
for name in names_counter:
    print(f'{name}: {names_counter[name]}')
print('----------')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]


def most_common_name(counter):
    return names_counter.most_common()[0]


names_counter = student_names_counter(students)
name, count = most_common_name(names_counter)
print(f'Самое частое имя среди учеников: {name}')
print('----------')

# Задание 3
# Есть список учеников в нескольких классах,
# нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for students in school_students:
    class_number = school_students.index(students) + 1
    names_counter = student_names_counter(students)
    name, count = most_common_name(names_counter)
    print(f'Самое частое имя в классе {class_number}: {name}')
print('----------')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {
        'class': '2a',
        'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {
        'class': '2б',
        'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {
        'class': '2б',
        'students': [
            {'first_name': 'Даша'},
            {'first_name': 'Олег'},
            {'first_name': 'Маша'}
        ]
    },
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


def count_genders_in_school(school, is_male_names):
    for school_class in school:
        students = school_class['students']
        genders = [is_male_names[dct['first_name']] for dct in students]
        genders_counter = Counter(genders)
        school_class['boys'] = genders_counter[True]
        school_class['girls'] = genders_counter[False]


count_genders_in_school(school, is_male)
for school_class in school:
    class_number = school_class['class']
    boys = school_class['boys']
    girls = school_class['girls']
    print(f'Класс {class_number}: девочки {girls}, мальчики {boys}')
print('----------')

# Задание 5
# По информации о учениках разных классов нужно найти класс,
# в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {
        'class': '2a',
        'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]
    },
    {
        'class': '3c',
        'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]
    },
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


def most_common_gender(school, gender):
    gender_counter = Counter({cls['class']: cls[gender] for cls in school})
    most_common_gender, _ = gender_counter.most_common(1)[0]
    return most_common_gender


count_genders_in_school(school, is_male)
boys = most_common_gender(school, 'boys')
girls = most_common_gender(school, 'girls')
print(f'Больше всего мальчиков в классе {boys}')
print(f'Больше всего девочек в классе {girls}')
