# Переменные:
# PassengerId - id пассажира
# Survived - бинарный показатель, выжил пассажир или нет (1 - выжил, 0 - не выжил)
# Pclass - класс пассажира
# Name - имя пассажира
# Sex - пол пассажира
# Age - возраст пассажира
# SibSp - число родных братьев/сестер пассажира на борту корабля (или супругов)
# Parch - число родителей пассажира на борту корабля
# Ticket - номер билета
# Fare - стоимость билета
# Cabin - каюта
# Embarked - порт, в котором пассажир взошел на палубу корабля


# Загрузка и предварительная обработка
# 1. Загрузите базу данных из файла Titanic.csv .
# 2. Загрузите базу данных так из файла еще раз, но так, чтобы столбец PassengerId был
# идентификатором, то есть номером строки (index).
# 3. Удалите из базы строки с пропущенными значениями и сохраните изменения в самой базе.



import pandas as pd
# 1
df = pd.read_csv('Titanic.csv')
print(df.head(10))

# 2
df_ind = pd.read_csv("Titanic.csv", index_col='PassengerId')
print(df_ind.head(10))
df.to_excel('output1.xlsx', index=False)

# 3
df_ind.dropna(inplace = True)
df_ind.to_excel('output2.xlsx', index=True)


