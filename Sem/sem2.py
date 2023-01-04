# N = 5: 1, -3, 9, -27, 81

# number = int(input('Введите целое число: '))

# for i in range(number):
#     print((-3)**i, end=' ') # Выводит в строку через пробел

# Задача 1
# # Напишите программу которая на вход будет принимать число N и выводить числа от -N до N
# # Вар 1
# # number = int(input('Введите число N:'))

# # for i in range(-number, number+1):
# #     if i == number:
# #         print(i)
# #     else:
# #         print(i, end = ", ")
# # Вар 2
# number = int(input('Введите число N:'))

# my_list = []

# for i in range(-number, number+abs(number)//number, abs(number)//number):
#     my_list.append(i)

# print(*my_list, sep=", ")



# Задача 2 Напишите программу которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# Вариант 1
# n = float(input('Введите число: '))

# if (int(n) == n):
#     print('Нет!')
# else:
#     print(int(abs(n) * 10 % 10))

# Вариант 2
number = float(input('Введите вещественное число: '))

if number != int(number):
    print(f'Первая цифра дробной части числа {number} -> {int(abs(number)*10)%10}')
else:
    print(f'У числа {int(number)} нет дробной части')
