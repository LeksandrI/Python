# Задача 6
# В некотором царстве, в некотором государстве, налог на доходы физических лиц вычисляется следующим образом. Базовая ставка налога составляет 13%. Если в
# каком-то месяце ваш заработок за год составит больше тысячи тугриков, то на оставшуюся часть года (не включая этот месяц) устанавливается ставка в 20%.
# Например, если вы зарабатываете каждый месяц 150 тугриков, то к июлю заработаете 150 на 7 = 1050 тугриков и начиная с августа подоходный налог будет
# начисляться по ставке 20%. Написать функцию calculate_tax(income), принимающую на вход массив, содержащий доход за каждый месяц года, начиная с
# первого и возвращающую общую сумму налога, который предстоит заплатить за год. Год в некотором царстве может длиться более 12 месяцев, если по этому
# поводу будет принят соответствующий высочайший декрет.

# Подсказка. Вам поможет функция np.cumsum(). Чтобы создать новый массив, длина которого равна длине какого-то другого, можно использовать функции np.zeros_like() или np.ones_like().

from timeit import timeit
import numpy as np

def calculate_tax(income):
    total = 0
    for i in range(len(income)):
        total  += income[i]
        if total  > 1000:
            summ = i + 1
            break
    if total  > 1000:
        result = np.sum(income[0:summ]) * 0.13 + np.sum(income[summ:]) * 0.2
    else:
        result = np.sum(income) * 0.13
    return result


income_array = [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]
print("Общий налог:", calculate_tax(income_array))


# Тестирование
assert np.isclose(calculate_tax(np.array([150]*12)), 286.5)
assert np.isclose(calculate_tax(np.array([100]*12)), 163)
assert np.isclose(calculate_tax(np.array([50]*12)), 78)
assert np.isclose(calculate_tax(np.array([1000]*12)), 2260)
assert np.isclose(calculate_tax(np.array(range(12))*100), 1215)
assert np.isclose(calculate_tax(np.array(range(11,-1,-1))*100), 1243)

def dummy(x):
    z = 0
    for y in x:
        z += y
        z += y*0.12
        if z:
            z += y
    return z

assert np.isclose(calculate_tax(np.array(range(12))*100), 1215)

N = int(1E6)
arr = np.array([1]*N)
benchmark = timeit("calculate_tax(arr)", "from __main__ import calculate_tax, arr", number=1)
reference_benchmark = timeit("dummy(arr)", "from __main__ import dummy, arr", number=1)

assert reference_benchmark > benchmark*5, "Код работает слишком медленно — вы точно использовали методы numpy?"