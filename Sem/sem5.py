data = '1 2 3 4 5 6 8 9 11'
data= list(map(int, data.split()))


'''
for i in range(len(new_data) - 1):
    if not new_data[i] + 1 == new_data[i+1]:
        print(new_data[i] + 1)
'''

my_func = list(filter(lambda i: not data[i] + 1 == data[i+1], range(len(data) - 1)))

for item in my_func:
    print(data[item] + 1)