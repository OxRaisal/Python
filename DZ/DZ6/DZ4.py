# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
my_list = list(map(int, input('Введите числа, через пробел: ').split()))
print(sum(my_list[1::2]))