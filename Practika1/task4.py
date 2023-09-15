# Напишите программу, которая принимает на вход список L, в котором хранятся значения доходов
# домохозяйств за месяц, а возвращает новый список L2 ‒ список логарифмированных значений доходов

nums = input("Напишите значение доходов за месяц: ")
tip = nums.split()

import math

numbers = [int(i) for i in tip]

list1 = [math.log(i) for i in numbers]
print(list1)

# list1 = []
# for i in numbers:
# list1.append(math.log(i))
# print(list1)