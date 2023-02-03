def main_menu() -> int:
    menu_list = ['Показать все контакты',
     'Открыть файл',
     'Сохранить файл',
     'Создать контакт',
     'Изменить контакт',
     'Удалить контакт',
     'Выход'
     ]
    for i in range(len(menu_list)):
        print(f'{i+1}. {menu_list[i]}')
    user_input = input('Введите команду:> ')
    # TODO: сделать валидацию
    return user_input

def show_all(db: list):
    for i in range(len(db)):
        user_id = i + 1
        print(user_id, end=' ')
        for k, v in db[i].items():
            print(k, v, end='; ')


    