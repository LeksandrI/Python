# Задача 3
# Напишите функцию str_lower() , которая принимает на вход строку (набор слов через пробел), а
# возвращает список ее элементов в нижнем регистре.
# Пример:
# Входные данные:
# "В лесу родилась ёлочка В лесу она росла"
# Выходные данные:
# ['в', 'лесу', 'родилась', 'ёлочка', 'в', 'лесу', 'она', 'росла']

def str_lower(tekst):
    spis = []
    low_reg = tekst.split()
    for kol in low_reg:
       spis.append(kol.lower())
    return spis

input_tekst = str(input("Введите текст: "))
res = str_lower(input_tekst)
print(res)
