# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

import logic, menu, log


def view(dict):
    for key in dict:
        print(f'{key} - {dict[key]}')

def main():
    catalog = {}
    catalog = logic.fill_first_dict(catalog)
    view(menu.ui_menu())
    logic.import_to_line(catalog)
    logic.import_by_line(catalog)

if __name__ == "__main__":
    main()