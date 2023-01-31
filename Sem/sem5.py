# Задача 1

# data = '1 2 3 4 5 6 8 9 11'
# data= list(map(int, data.split()))


# '''
# for i in range(len(new_data) - 1):
#     if not new_data[i] + 1 == new_data[i+1]:
#         print(new_data[i] + 1)
# '''

# my_func = list(filter(lambda i: not data[i] + 1 == data[i+1], range(len(data) - 1)))

# for item in my_func:
#     print(data[item] + 1)

# Задача 2

# data = [1, 5, 2, 3, 4, 6, 1, 7]
# result = []
# count = 0
# num1 = 1
# while count < len(data):
#     for i in range(len(data) - 1):
#         temp = []
#         temp.append(data[i])
#         cur_max = data[i]
#         for j in range(num1, len(data)):
#             if data[j] > cur_max:
#                 temp.append(data[j])
#                 cur_max = data[j]
#         if len(temp) > 1 and temp not in result:
#             result.append(temp)
#     count += 1
#     num1 += 1

# print(result)

# Задача 3
from string import punctuation
my_str = 'АБВ ваываыв ваыва! абв? 3ваав вабв34, вава абВ'
res = []

x = 'абв'
for c in punctuation:
    my_str = my_str.replace(c, ' ' + c + ' ')
data = my_str.split()
print(data)

for item in data:
    if not x.lower() in item.lower():
        res.append(item)
res = ' '.join(res)
for c in punctuation:
    res = res.replace(' ' + c, c)
print(res)


# my_str = 'АБВ ваываыв ваыва! абв& 3ваав вабв34, вава абВ'
# res = []
# chars = ['.', ',','!','?']
# x = 'абв'
# for c in chars:
#     my_str = my_str.replace(c, ' ' + c + ' ')
# data = my_str.split()
# print(data)

# for item in data:
#     if not x.lower() in item.lower():
#         res.append(item)
# print(' '.join(res))