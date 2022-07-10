# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def show_number_plane(x, y):
    if x > 0 and y > 0:
        print('1')
    elif x < 0 and y > 0:
        print('2')
    elif x < 0 and y < 0:
        print('3')
    elif x > 0 and y < 0:
        print('4')
    else:
        print('Не могу определить положение. X или Y равны 0')

def main():
    x = int(input('Введите X - '))
    y = int(input('Введите Y - '))
    show_number_plane(x, y)

if __name__ == "__main__":
    main()