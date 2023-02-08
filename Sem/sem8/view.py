num_class = ''


def main_menu():
    print('\n======Журнал успеваемости учеников======\n')
    print('Варианты доступа к журналу: ')
    menu_list = [
        'Родители',
        'Учителя',
    ]

    for i, item in enumerate(menu_list):
        print(f'\t{i + 1}. {item}')


def choice_access() -> int:
    while True:
        try:
            access = int(input('\nВведите порядковый номер доступа: '))
            if access not in [1, 2]:
                print('Введите 1 или 2!')
            elif access in [1, 2]:
                return access
        except ValueError:
            print('Некорректный ввод! Введите число 1 или 2.')


def choice_class() -> str:
    global num_class
    while True:
        try:
            class_num = input('\nВведите класс: ')
            if class_num.lower() not in ['7а', '7б']:
                print('Доступны класс 7А или класс 7Б')
            elif class_num.lower() in ['7а', '7б']:
                path = class_num.upper() + '.txt'
                num_class = class_num

                return path
        except ValueError:
            print('Некорректный ввод! Введите число 1 или 2.')


def show_journal(journal: dict):
    print(f'\nУспеваемость учеников в {num_class.upper()} классе:\n')
    for key in journal.keys():
        print(f'{key}:')
        j = 0
        for i, item in journal[key].items():
            j += 1
            print(f'\t{j}. {i}: ', end=' ')
            print(*item)
        print()


def menu_parents():
    print('\n========== Успеваемость ученика ==========\n')
    menu_list = [
        'Успеваемость по всем предметам',
        'Успеваемость по конкретному предмету',
        'Выход',
    ]

    for i, item in enumerate(menu_list):
        print(f'\t{i + 1}. {item}')


def command_parents() -> int:
    while True:
        try:
            menu_parents()
            command = int(input('\nВведите номер команды: '))
            if command < 1 or command > 3:
                print('Введите номер команды от 1 до 3!')
            else:
                return command
        except ValueError:
            print('Некорректный ввод! Введите число 1 или 3.')


def get_name() -> str:
    name = input('Введите фамилию и имя ученика через пробел: ')
    print()
    return name.title().strip()


def get_lesson() -> str:
    lesson = input('Введите название предмета: ')
    print()
    return lesson.capitalize().strip()


def show_message(text: str):
    print(text)


def show_pupil_lessons(journal: dict, name: str):
    print(f'Ученик {num_class.upper()} класса {name}')
    for key in journal.keys():
        print(f'\t{key}:', end=' ')
        for i, item in journal[key].items():
            if i == name:
                print(*item)


def show_pupil_lesson(journal: dict, name: str, lesson: str):
    print(f'Ученик {num_class.upper()} класса {name}')
    print(f'\t{lesson}: ', end=' ')
    print(*journal[lesson][name])


def menu_teacher():
    menu_list = [
        'Список всех учеников',
        'Успеваемость всех учеников по всем дисциплинам',
        'Успеваемость учеников по предмету',
        'Контроль знаний ученика',
        'Выход',
    ]

    print('\n=========== Главное меню ===========')
    for i, item in enumerate(menu_list):
        print(f'\t{i + 1}. {item}')


def command_teacher() -> int:
    while True:
        try:
            menu_teacher()
            command = int(input('\nВведите номер команды: '))
            if command < 1 or command > 5:
                print('Введите номер команды от 1 до 5!')
            else:
                return command
        except ValueError:
            print('Некорректный ввод! Введите число 1 или 5.')


def show_list_pupils(journal: dict):
    print(f'\nСписок всех учеников в {num_class.upper()} классе: ')
    for item in journal.values():
        i = 0
        for key in item.keys():
            i += 1
            print(f'\t{i}. {key}')
        break


def show_progress_lesson(journal: dict, lesson: str):
    print(f'\nУспеваемость учеников {num_class.upper()} класса')
    print(f'Дисциплина: {lesson.lower()}\n')
    i = 0
    for key, value in journal[lesson].items():
        i += 1
        print(f'\t{i}. {key}: ', end=' ')
        print(*value)


def control() -> int:
    while True:
        try:
            mark = int(input('Введите полученную отметку: '))
            if mark not in [1, 2, 3, 4, 5]:
                print('Введите отметку от 1 до 5.')
            elif mark in [1, 2, 3, 4, 5]:
                return mark
        except ValueError:
            print('Некорректный ввод! Введите число 1 или 5.')