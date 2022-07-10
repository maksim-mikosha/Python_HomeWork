# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def enter_value(coordinate, name):
    print(f'Введите координату {coordinate} точки {name} - ')
    return int(input())

def calculation_distance(xA, yA, xB, yB):
    diffX = xB - xA
    diffY = yB - yA
    return (diffX ** 2 + diffY ** 2) ** 0.5

def main():
    xA = enter_value("x", "A")
    yA = enter_value("y", "A")
    xB = enter_value("x", "B")
    yB = enter_value("y", "B")
    distance = round(calculation_distance(xA, yA, xB, yB), 2)
    print(f'Расстояние между точками равно - {distance}')

if __name__ == "__main__":
    main()