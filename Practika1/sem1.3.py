# Дан список L. Выведите на экран (последовательно, с новой строчки):
# все элементы списка L
# логарифмированные значения элементов списка L

L = [12, 3, 8, 125, 10, 98, 54, 199]

for i in L:
    print(i)

import math

for i in L:
    print(math.log(i))

# Замените пятый элемент списка L на 0. Проделайте те же операции, что и раньше. Объясните, почему
# получаются такие результаты.
L = L.copy()
L[4] = 0
print(L)


for i in L:
    print(i)

for i in L:
    print(math.log(i))