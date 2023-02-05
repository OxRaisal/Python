import model
import view

model.read_db('database.txt')
user_inp = view.main_menu()
# print(temp)

def input_handler(inp: int):
    match inp:
        case 1:
            view.show_all(model.db_list)
        case 2:
            model.read_db('database.')

while True:
    user_inp = view.main_menu()
    input_handler(user_inp)


            #  1.35.36