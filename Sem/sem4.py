                    # Словарь
# my_dict = {}

# number = int(input('Введите целое число: '))

# for n in range(1, number+1):
#     my_dict[n] = 3*n + 1

# print(my_dict.get(4, 'Такого ключа нет'))

                    # Строки

# my_string = 'Питон самый лучший язык в мире'
#                                                          #
# my_string = my_string.replace('и', '$')                  #split спиливает строку по заданному элементу('и')
# print(my_string)                                         #replace заменяет('и', '$')
# my_list = ['1','2','34','5','6','7','8']
# glue = ''
# print(glue.join(my_list))
# print(my_string)

# Задача 1. Найдите корни квадратного уравнения Ax^2 + Bx + C = 0
import math


equation = '3*x**2 + 5*x - 6 = 0'
def create_koef(equation: str):
    new_equation = equation.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -')
    new_equation = new_equation.split()
    new_list = []
    for item in new_equation:
        if item.startswith('x'):
            new_list.append(1)
        elif item.startswith('-x'):
            new_list.append(-1)
        else:
            new_list.append(item.split('*x')[0])
    return new_list

def solve_equation(koef):
    a, b, c = int(koef[0]), int(koef[1]), int(koef[2])
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x1 = (-b - math.sqrt(disc)) / (2 *a)
        x2 = (-b + math.sqrt(disc)) / (2 *a)
        return round(x1, 2), round(x2, 2)
    elif disc == 0:
        x = (-b - math.sqrt(disc)) / (2 *a)
        return round(x, 2)
    else:
        return None

print(create_koef(equation))
print(solve_equation(create_koef(equation)))





# equation = '3*x**2 + 5*x - 6 = 0'
# equation = equation.replace('x**2','')
# equation = equation.replace('*','')
# equation = equation.replace('x','')
# equation = equation.replace('= 0','')
# equation = equation.rstrip()
# equation = equation.split(' ')

# a = int(equation[0])
# b = int(equation[2])
# c = int(equation[4])

# if equation[1] == '-':
#     b *= -1
# if equation[3] == '-':
#     c *= -1
# print(a, b, c)

# discriminant = b**2 - 4*a*c

# def function (d):
#     if d < 0:
#         return('Решений нет')
#     elif d == 0:
#         return(-(b/(2*a)))
#     else:
#         return [(-b + (discriminant)**0.5)/(2*a), (-b - (discriminant)**0.5)/(2*a)]
# z = function (discriminant)
# print(z)

# if discriminant < 0:
#     print('Решений нет')
# elif discriminant == 0:
#     print(-(b/(2*a)))
# else:
#     x1 = round((-b + (discriminant)**0.5)/(2*a),3)
#     x2 = round((-b - (discriminant)**0.5)/(2*a),3)
#     print(f'x1 = {x1}, x2 = {x2}')




