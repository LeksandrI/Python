# Задача 3
# Напишите программу, которая запрашивает у пользователя пароль, и далее:
# если пароль верный, выводит на экран сообщение "Login success".
# если пароль неверный, выводит на экран сообщение "Incorrect password, try again!" до тех пор, пока
# пользователь не введет верный пароль.

Password = 1234

while True:
    Pas = int(input("Введите пароль: "))
    if Pas == Password:
        print("Login success ")
        break
    else:
        print("Incorrect password, try again!")
