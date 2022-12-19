# типы данных и переменная
# int, float, boolean, str, list, None
#value = None
#print(type(value))

#a = 123
#b = 1.23
#print(type(a))
#print(type(b))
#value = 12334
#print(type(value))
#s = "Hello 'World"
#print(s)
#s = 'Hello "World'
#print(s)
#s = 'Hello \'World'
#print(s)
#s = "Hello \nWorld"
#print(s)
#print(a, b, s)
#print(a, '-', b, '-', s)
#print('{} - {} - {} '.format(a, b, s))
#print(f'{a} - {b} - {s} ')
#print('{1} - {2} - {0} '.format(a, b, s))

#f = True
#print(f)
#list = ['1', '2', '3', 'Hello']
#col = ['Hello', 1,2,4.5,True]
#print(list)
#print(col)

#int - целые числа
#print('Введите a')
#a = int(input())
#print('Введите b')
#b = int(input())
#print(a, b)
#rint('{} {}'.format(a, b))
#print(f'{a} {b}')
#print(a,' ', b, ' = ', a+b)

#float - дробные числа
#print('Введите a')
#a = float(input())
#print('Введите b')
#b = float(input())
#print(a,' ', b, ' = ', a+b)



#  Арифметические действия

#a =2
#b = 8
#c=a+b
#print(c)

#a = 1.32312
#b = 3
#c = round(a * b, 5)
#print(c)

#a = 3
#a = a + 5
#print(a)



#           Логические операции

# a = 1 < 4
# print(a)
# a = [1,2]
# b = [1,2]
# print (a == b)

# func = 1
# T = 4
# X = 2

# print(func<T>(X))

# f = 1 > 2 or 4 < 6

# print(f)

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# #is_odd = not f[0] % 2
# print(is_odd)



#        Управляющие конструкции  if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)



# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала вас, МАРИНА!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)





#        While

# original = 2323
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)




#        While-else


# original = 2323
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)



#                for


# list = [1,2,3,10,5]
# for i in list:
#     print(i)


# r = range(10) # (1,5), (1, 10, 2)
# for i in r:
#     print(i)


# for i in 'qwe - rty':
#     print(i)



# #                Строки


# # text = 'съешь еще этих мягких французских булок'

# # help(text.istitle)


# text = 'съешь еще этих мягких французских булок'
# print(text[0])                                   # с
# print(text[1])                                   # ъ
# #print(text[len(text)])                            # indexError
# print(text[len(text)-1])                         # к
# print(text[-5])                                  # б
# print(text[:])                                   #  print(text)
# print(text[:])                                   # съ
# print(text[len(text)-2:])                        # ок
# print(text[2:9])                                 # ешь еще
# print(text[6:-18])                               # еще этих мягких
# print(text[0:len(text):6])                       # сеикакл
# print(text[::6])                                 # сеикакл
# text = text[2:9] + text[-5] + text[:2]           # 






#                           Списки: введение

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *=2
#     print(i)
# print(numbers)



# colors = ['red', 'green', 'blue']

# for e in colors:       
#     print(e)               #red green blue

# for e in colors:
#     print(e*2)             # redred greengreen blueblue

# colors.append('gray')              #добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])   #true
# colors.remove('red')    # del colors[0]  #удалить элемент



#                       Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))









