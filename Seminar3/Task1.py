# Задача 1
# Напишите программу, которая просит пользователя ввести положительное число, и если пользователь
# вводит положительное число, выводит на экран сообщение "Молодец!", если нет ‒ "Это не
# положительное число.".
# Считайте, что пользователь в любом случае вводит числа, а не какой-то текст.


x = int(input("Введите положительное число: "))
if x > 0:
    print("Молодец ")
else:
    print("Это не положительное число ")