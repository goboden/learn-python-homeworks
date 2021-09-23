# stops.csv = https://data.mos.ru/datasets/752

import csv
from collections import Counter


streets = []

with open('stops.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        streets.append(row['Street'])
streets_counter = Counter(streets)

most_common_street, _ = streets_counter.most_common(1)[0]
print(f'Больше всего остановок на улице "{most_common_street}"')
