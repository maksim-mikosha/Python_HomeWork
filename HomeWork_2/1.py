# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


def format_list(list):
    if '-' in list:
        list.remove('-')

    if '.' in list:
        list.remove('.')
    elif ',' in list:
        list.remove(',')

def main():
    input_list = list(input('Введите значение - '))
    summary = 0
    format_list(input_list)
    for i in range(len(input_list)):
        summary += int(input_list[i])
        
    print(f'Сумма цифр - {summary}')

if __name__ == "__main__":
    main()