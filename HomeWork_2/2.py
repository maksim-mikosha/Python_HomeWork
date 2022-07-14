# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def factorial(number):
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    return factorial

def main():
    input_number = int(input('Введите число - '))
    print(f'Факториал числа {input_number} = {factorial(input_number)}')

if __name__ == "__main__":
    main()