# Задача 4
# Написать функцию weighted_sum(weights, grades, normalize), возвращающую взвешенную сумму оценок, записанных в массив grades, в соответствии с
# весами, записанными в массив weights. Например, для weights = np.array([0.3, 0.3, 0.4]) и grades = np.array([7, 9, 8]) функция должна вернуть число 8.0.
# Если параметр normalize установлен в True, а сумма всех весов отличается от 1, то следует умножить все веса на одно и то же число таким образом, чтобы их
# сумма была равна 1, в противном случае следует использовать веса «как есть», даже если их сумма отличается от 1. Если функция запущена без указания параметра 
# normalize, следует считать, что normalize = False.

# Подсказка: Вам помогут функции np.dot() и np.sum(). Встроенная функция sum() также работает с массивами numpy, но гораздо медленнее (проверьте с помощью %timeit!)

from timeit import timeit
import numpy as np

def weighted_sum(weights, grades, normalize):
    if normalize:
        total_weight = np.sum(weights)
        if total_weight != 1:
            weights = weights * (1 / total_weight)
    return np.dot(weights, grades)

weights = np.array([0.3, 0.3, 0.4])
grades = np.array([7, 9, 8])

normalize = True
print(weighted_sum(weights, grades, normalize))



# Тестирование
def test(w, g, out, normalize = False):
    q = weighted_sum(np.array(w), np.array(g), normalize)
    assert np.isclose(q, out)

test([0.3, 0.3, 0.4], [7, 9, 8], 8)
test([0.1, 0.2, 0.3, 0.4], [1, 5, 3, 2], 2.8)
test([1, 2, 3, 4], [1, 5, 3, 2], 28)
test([1, 2, 3, 4], [1, 5, 3, 2], 2.8, normalize=True)

N = 1000000

test([1, 2, 3, 4], [1, 5, 3, 2], 28)

benchmark = timeit("sum([x/x for x in np.array([1]*N)])", "from __main__ import N, np", number=1)
otherbenchmark = timeit("weighted_sum(np.array([1.1]*N), np.array([1]*N), True)", 
                        "from __main__ import N, weighted_sum, np", number=1)

print(benchmark/otherbenchmark)
assert benchmark > otherbenchmark*1.7, "Код работает слишком медленно — вы точно использовали методы numpy?"