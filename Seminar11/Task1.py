# Задача 1
# Написать функцию double_this(arr), принимающую на вход массив arr, состоящий из чисел, и возвращающую массив, полученный удвоением каждого элемента arr.
# Подсказка: Операции с массивами действуют поэлементно.

from timeit import timeit
import numpy as np

def double_this(arr):
    return np.array(arr) * 2

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(double_this(arr))


# Тестирование
def testme(f, inp, outp):
    q = f(np.array(inp))
    assert isinstance(q, np.ndarray), "Функция должна возвращать массив numpy (np.array)"
    assert np.array_equal(q, np.array(outp)), "Ошибка для входного списка "+str(np.array(inp))
def test(inp, outp):
    testme(double_this, inp, outp)

test([1, 2, 3], [2, 4, 6])
test([1.1, 2.2, 3.3], [2.2, 4.4, 6.6])
test([1]*10, [2]*10)
test([1]*10+[2]*15, [2]*10+[4]*15)

N = 1000000

benchmark = timeit("[x*x for x in np.array([1]*N)]", "from __main__ import N, np", number=1)
otherbenchmark = timeit("double_this(np.array([1]*N))", 
                        "from __main__ import N, np, double_this", number=1)
print(benchmark, otherbenchmark)
assert benchmark > otherbenchmark*2, "Код работает слишком медленно — вы точно не пользовались циклами?"