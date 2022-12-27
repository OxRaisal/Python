# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


number = int(input('Введите целое число: '))

total = 0
num_list = []
for i in range(1, number + 1):
    num = (1 + 1 / i) ** i
    if num - int(num) == 0:
        num = int(num)
    else:
        num = round(num, 2)
    num_list.append(num)
    total += num
print(f'n = {number} -> {num_list}\nСумма {total}')