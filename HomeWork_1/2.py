# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def enter_value(coordinate):
    return int(input(f'Введите координату {coordinate} - '))

def check_predicate(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    return left == right

def main():
    x = enter_value("x")
    y = enter_value("y")
    z = enter_value("z")
    if check_predicate(x,y,z):
        print("Утверждение истинно")
    else:
        print("Утверждение ложно")

if __name__ == "__main__":
    main()