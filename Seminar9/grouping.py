# Группировка
# 1. Выведите на экран все уникальные значения в столбце Embarked.
# 2. Сгруппируйте строки в датафрейме в соответствии со значениями переменной Survived и выведите
# средние значения всех количественных переменных по группам.
# 3. Сгруппируйте строки в датафрейме в соответствии со значениями переменной Sex и сохраните в
# отдельный датафрейм таблицу со средними и медианными значениями переменной Age по группам
# (мужчины и женщины).


import pandas as pd

df = pd.read_csv("Titanic.csv", index_col='PassengerId')
df.dropna(inplace = True)
#1
unik = df["Embarked"].unique()
print(unik)

#2
grouped_data = df.select_dtypes(include='number').groupby(df['Survived']).mean()

print(grouped_data)

#3
sexage = df.groupby('Sex')['Age'].agg(['mean', 'median'])
print(sexage)

