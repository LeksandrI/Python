# Задача 3
# Дан список, состоящий из пар чисел:
# Создайте словарь calc , где ключами являются пары чисел, а значениями – их произведение
# (произведение тоже должно считаться в Python, не в уме).

pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]

list = []

for pair in pairs:
    res = pair[0]*pair[1]
    list.append(res)

calc = dict(zip(pairs,list))
print(calc)







