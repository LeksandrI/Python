# Работа со строками и столбцами базы
# 7. Выведите названия столбцов в базе данных в виде списка (объект типа list).
# 8. Переименуйте столбец с классом пассажира из Pclass в Class.
# 9. Выберите из базы данных все строки, которые соответствуют пассажирам женского пола, и
# сохраните их в новую базу female .
# 10. Выберите из базы данных все строки, которые соответствуют выжившим пассажирам мужского пола
# младше 32 лет, и сохраните их в базу Ymale .
# 11. Выберите из базы данных все строки, которые соответствуют пассажирам 1 или 2 класса.
# 12. Выберите из базы данных все строки, которые соответствуют выжившим пассажирам 1 или 2 класса.
# 13. Добавьте в датафрейм столбец Female, состоящий из значений 0 и 1, где 1 соответствует
# пассажирам женского пола.

import pandas as pd
df = pd.read_csv('Titanic.csv')

#7
spisok = list(df.columns)
print(spisok)

#8
spisok[2]="Class"
df.columns = spisok
print(df.columns)

#9
female = df[df['Sex'] == 'female']
print(female)

female.to_excel("outputFemale.xlsx", index = False)

#10 
Ymale = df[(df['Sex'] == 'male') & (df['Age'] < 32) & (df['Survived'] == 1)]
print(Ymale)

Ymale.to_excel("outputMan.xlsx", index = False)

#11
Class = df[(df['Class'] == 1) | (df['Class'] == 2)]

Class.to_excel("outputClass.xlsx", index = False)

#12
SurvClass = df[((df['Class'] == 1) | (df['Class'] == 2)) & (df['Survived'] == 1)]

SurvClass.to_excel("outputSurvClass.xlsx", index = False)

#13
df['Female'] = df['Sex'].map({"female" : 1, "male" : 0})

df.to_excel("outputStolbec.xlsx", index = False)