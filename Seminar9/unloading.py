# Выгрузка базы в файл
# 1. Приведите все названия столбцов в датафрейме к нижнему регистру и сохраните изменения.
# 2. Выгрузите итоговый датафрейм в файл Titanic-new.csv.

import pandas as pd

df = pd.read_csv('Titanic.csv', index_col = 0)

#1
df.columns = df.columns.str.lower()
df.index.name = df.index.name.lower()
print(df)

#2

df.to_csv('Titanic.csv')