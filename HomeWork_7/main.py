# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

import logic, menu, log


def view(dict):
    for key in dict:
        print(f'{key} - {dict[key]}')

def main():
    catalog = {}
    catalog = logic.fill_first_dict(catalog)
    inputCommand = 0
    while inputCommand != 6:
        print('Список доступных комманд!')
        view(menu.ui_menu())
        inputCommand = int(input('Введи номер команды: '))
        if inputCommand == 0:
            catalog = logic.fill_test_dict(catalog)
            print('Вроде получилось)')
        elif inputCommand == 1:
            catalog = logic.add_to_file(catalog)
        elif inputCommand == 2:
            print('В разработке')
        elif inputCommand == 3:
            logic.import_by_line(catalog)
        elif inputCommand == 4:
            logic.import_to_line(catalog)
        else:
            view(catalog)
 
if __name__ == "__main__":
    main()