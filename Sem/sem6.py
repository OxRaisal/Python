from random import randint as RI

#1.  my_list = []

#       for i in range(10):
#       my_list.append(1)

#    my_list = [i for i in range(10)
# string = '1 2 3 45 6 7 8 9 07 457'
# string = string.split()
# my_list = [RI(0,10) for _ in range(10)]
# print(string)
#                          2 map
# string = '1 2 3 45 6 7 8 9 07 457'

# # for i in range(len(string)):
# #     string[i] = int(string[i])

# string = list(map(int, string.split()))
# string = list(map(lambda x: x**2, string))
# print(string)

#                           3 enumerate
# string = '1 2 3 45 6 7 8 9 07 457'
# string = string.split()

# for i, item in enumerate(string, 1):
#     print(f'{i} глава. "{item}"')

#                           4 zip
# nums = '1 2 3 4 5 6 7'
# letters = 'a b c d e f g'
# signs = '+ - # $ ^ & !'

# nums = nums.split()
# letters = letters.split()
# sings = signs.split()

# size = []
# size.append(len(nums))
# size.append(len(letters))
# size.append(len(signs))

# new_list = []
# for i in range(min(size)):
#     for k in range(len(size[i])):
#         new_list.append((nums[i], letters[i], signs[i]))

# print(new_list)

                                # 5 lammda

# calc = {'Сложение': lambda x, y: x + y}

# print(calc.get('Сложение')(4, 5))

#                                 6 Задание 1. Вывести не повторяющиеся числа

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# my_dict = {}

# for item in my_list:
#     my_dict[item] = my_dict.get(item, 0) + 1
#     print(my_dict)

# for key, value in my_dict.items():
#     if value == 1:
#             print(key)

#                                 7 Задание 2.

data_1 = '2+2'
data_2 = '1+2*3'
data_3 = '1-2*3'

data = data_3.replace('+', ' + ').replace('-', ' - ').replace('/', ' / ').replace('*', ' * ')
data = data.split()
print(data)

oper = {
     '+': lambda x, y: int(x) + int(y),
     '-': lambda x, y: int(x) - int(y),
     '/': lambda x, y: int(x) / int(y),
     '*': lambda x, y: int(x) * int(y),
}

def calc(data: list) -> int:
     for i in range(len(data)-1):
         if data[i] in '*/':
             operation = data[i]
             left = data[i-1]
             right = data[i+1]
             res = oper[operation](left, right)
             print(f'Результат операции {left} {operation} {right} = {res}')
             print('Новый список:', data[:i-1] + [str(res)] + data[i+1:])
             return data[:i-1] + [str(res)] + data[i+2:]
     for j in range(len(data) - 1):
         if data[j] in '+-' and j != 0:
             operation = data[i]
             left = data[j-1]
             right = data[j+1]
             res = oper[operation](left, right)
             print(f'Результат операции {left} {operation} {right} = {res}')
             print('Новый список:', data[:i-1] + [str(res)] + data[i+1:])
             return data[:j-1] + [str(res)  ] + data[j+2:]
         
for item in oper.keys():
     while item in data:
         data = calc(data)

print(data[0])
