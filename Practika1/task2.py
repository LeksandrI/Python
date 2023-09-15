# Напишите программу, которая берет строку "1; 2; 3; 100" и возвращает:
# список из целых чисел
# список из чисел с плавающей точкой

string = '1; 2; 3; 100'

list1 = []
for k in string.split(";"):
    list1.append(int(k))
print(list1)

list1 = []
for k in string.split(";"):
    list1.append(float(k))
print(list1)