# Напишите программу которая принимает на вход 2 числа и проверяет, является одно число корнем другого
# num1 = int(input('num1 = '))
# num2 = int(input('num2 = '))
# if num1 == num2**2 or num2 == num1**2:
#     print('да')
# else:
#     print('нет')


# Напишите программу, которая принимает на вход 5 чисел и находит максимальное  из них

nums = []
for i in range(5):
    number = int(input('Введиите число: '))
    nums.append(number)

#1
# my_max = nums[0]
# for item in nums:
#     item = 6
# print(nums)

# for i in range(len(nums)):
#     nums[i] = 6
# print(nums)

#2
my_max = nums[0]
for item in nums:
    if my_max < item:
        my_max = item

print(f'Максимальное значение списка {my_max}')




