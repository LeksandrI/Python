# Задача № 2
# Составьте 2 списка чисел из своего и любого другого мобильного номера телефона. Нужно получить
# новый список, состоящий из элементов, равных произведению соответствующих элементов
# первоначальных списков. Решить эту задачу при помощи функции map() и lambda-функции.

my_number = [8,8,1,1,5,5,5,3,5,3,5]
other_number = [8,9,2,6,5,8,1,1,2,4,7]

result = list(map(lambda x,y: x*y, my_number, other_number))

print(result)