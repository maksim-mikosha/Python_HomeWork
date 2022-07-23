# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.


from random import randint

def create_polynom(number):
    polynom = ''
    for i in reversed(range(0, number + 1)):
        rand = randint(0, 10)
        if rand != 0:
            if i == 0:
                polynom += str(rand)
            elif i == 1:
                polynom += str(rand) + '*x + '
            else:
                polynom += str(rand) + '*x^' + str(i) + ' + '
    polynom += ' = 0'
    return polynom

def main():
    input_number = int(input('Введите степень для многочлена - '))
    print(f'Случайно сгенерированный многочлен для степени {input_number} - {create_polynom(input_number)}')

if __name__ == "__main__":
    main()