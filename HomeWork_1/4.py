# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def show_plane_range(quarter):
    if quarter == 1:
        print(f'Диапазон координат для четверти {quarter} : X от 1 до max - Y от 1 до max')
    elif quarter == 2:
        print(f'Диапазон координат для четверти {quarter} : X от min до -1 - Y от 1 до max')
    elif quarter == 3:
        print(f'Диапазон координат для четверти {quarter} : X от min до -1 - Y от min до -1')
    elif quarter == 4:
        print(f'Диапазон координат для четверти {quarter} : X от 1 до max - Y от min до -1')
    else:
        print('Неправильно введен номер четверти')

def main():
    quarter = int(input('Введите номер плоскоти - '))
    show_plane_range(quarter)

if __name__ == "__main__":
    main()