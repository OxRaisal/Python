import os, random

min_degree = 2
max_degree = 5

def convert_degree(degree: int):
    result = ''
    while degree:
        result = dict_degrees[degree % 10] + result
        degree //= 10
    return result

def create_an_equation_from_dict(k: int):
    members_list = []
    for i in range(k, -1, -1):
        rnd_int = random.randint(-10, 10)
        if rnd_int == 0:
            continue
        else:
            coeff = str(rnd_int)
        if i in (0, 1):
            x = 'X' * i
        else:
            x = f'X{convert_degree(i)}'
        members_list.append(coeff + x)
    equation = ' + '.join(members_list)\
        .replace('1X', 'X')\
        .replace(' + -', ' - ')\
        + ' = 0'
    return equation

dict_degrees = \
    {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}

if __name__ == '__main__':
    run_path = os.path.abspath(__file__)
    dir_path = run_path[:run_path.rindex('\\') + 1]
    
    with open(dir_path + 'input_1.txt', 'w', encoding='UTF-8')  as file:
        k = random.randint(min_degree, max_degree)
        new_data = create_an_equation_from_dict(k)
        file.write(new_data)
    
    with open(dir_path + 'input_2.txt', 'w', encoding='UTF-8')  as file:
        k = random.randint(min_degree, max_degree)
        new_data = create_an_equation_from_dict(k)
        file.write(new_data)