import csv


person_jobs = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]


def get_header(dict_list):
    header = set()
    for dct in dict_list:
        for key in dct:
            header.add(key)
    return header


def write_csv(filename, header, data):
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, header, delimiter=';')
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    header = get_header(person_jobs)
    write_csv('dict_list.csv', header, person_jobs)


if __name__ == '__main__':
    main()
