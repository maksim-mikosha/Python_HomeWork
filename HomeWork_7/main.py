# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

import logic, menu

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
            confirm = input('Данное действие перезапишет текущий каталог! Уверен? yes/no ')
            if confirm == 'yes':
                catalog = logic.fill_test_dict(catalog)
                print('Вроде получилось)')
            elif confirm == 'no':
                print('Отмена!!!')
            else:
                print('Я не понял, но на всякий случай отменил.')
        elif inputCommand == 1:
            catalog = logic.add_to_file(catalog)
        elif inputCommand == 2:
            view(catalog)
            input_update_value = input('Введи номер строки для изменения или no для отмены - ')
            if input_update_value == 'no':
                print('Отмена!!!')
            elif input_update_value == '0':
                print('Невозможно изменить заголовок')
                print('Отмена!!!')
            else:
                catalog = logic.update_value(catalog, input_update_value)
        elif inputCommand == 3:
            logic.import_by_line(catalog)
        elif inputCommand == 4:
            logic.import_to_line(catalog)
        elif inputCommand == 5:
            view(catalog)
        else:
            print('Пока-пока!')
 
if __name__ == "__main__":
    main()