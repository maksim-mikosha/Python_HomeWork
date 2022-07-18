# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


def main():
    string = input('Введите список из чисел разделяя пробелами - ').split(' ')
    tempstring = string[1::2]
    summary = 0
    for i in tempstring:
        summary += int(i)
    print(f'Сумма нечетных элементов списка = {summary}')

if __name__ == "__main__":
    main()