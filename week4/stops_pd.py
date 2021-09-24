# stops.csv = https://data.mos.ru/datasets/752

import pandas as pd


stops_df = pd.read_csv(open('stops.csv', 'r', encoding='cp1251'), sep=';')

# print(f'Больше всего остановок на улице "{most_common_street}"')
