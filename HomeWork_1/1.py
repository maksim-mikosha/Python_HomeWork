# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def show_week_day(number):
    if 6 <= number <= 7:
        print('Да')
    elif 1 <= number <= 5:
        print('Нет')
    else:
        print('Упс, что-то пошло не так :(')

def main():
    show_week_day(number = int(input('Введите день недели - ')))

if __name__ == "__main__":
    main()