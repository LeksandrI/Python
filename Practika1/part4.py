# У вас есть шаблон, похожий на шаблон рецепта из предыдущей задачи:
# Рецепт
# политическая теория : __ кг
# история политических учений: __ кг
# математика: __ кг
# Приправить политической историей. Добавить математические модели по вкусу.
# Напишите программу, которая запрашивает у пользователя три значения массы ингредиентов в граммах
# (три вопроса), переводит их в килограммы и подставляет полученные значения в шаблон так, чтобы
# числа содержали ровно 3 знака после запятой

first = int(input("Введите значение массы ингредиента в граммах: "))
second = int(input("Введите значение массы ингредиента в граммах: "))
third = int(input("Введите значение массы ингредиента в граммах: "))
kilo1 = first/1000
kilo2 = second/1000
kilo3 = third/1000

print("Политическая теория : %.3f кг." % (kilo1))
print("История политических учений : %.3f кг." % (kilo2))
print("Математика : %.3f кг." % (kilo3))