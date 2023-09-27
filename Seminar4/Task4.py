# Задача 4
# Дан словарь grades с оценками студентов за контрольную работу в 5-балльной шкале. Напишите код,
# который сделает следующее:
# Выведет на экран имя каждого студента и его оценку (каждый студент – с новой строки).
# Сохранит имена студентов, получивших отличные оценки, в список excel .
# Сохранит имена студентов, получивших хорошие оценки, в список good .
# Сохранит имена студентов, получивших удовлетворительные оценки, в список satisf .
# Сохранит имена студентов, получивших плохие оценки, в список bad .

# Выведет на экран имя каждого студента и его оценку (каждый студент – с новой строки).
grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5, 'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2, 'Ursula': 4, 'Viktor': 5}

for name, marks in grades.items():
    print(name,marks)

# Сохранит имена студентов, получивших отличные оценки, в список excel .
exel = []

for name, marks in grades.items():
    if marks == 5:
        exel.append(name)
print('Отличные оценки: ',exel)

# Сохранит имена студентов, получивших хорошие оценки, в список good .
good = []
for name, marks in grades.items():
    if marks == 4:
        good.append(name)
print('Хорошие оценки: ',good)

# Сохранит имена студентов, получивших удовлетворительные оценки, в список satisf .
satisf = []
for name, marks in grades.items():
    if marks == 3:
        satisf.append(name)
print('Удовлетворительные оценки: ', satisf)

# Сохранит имена студентов, получивших плохие оценки, в список bad .
bad = []
for name, marks in grades.items():
    if marks == 2:
        bad.append(name)
print('Плохие оценки: ', bad)

