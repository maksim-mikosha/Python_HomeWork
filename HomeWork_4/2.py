# Задайте натуральное число N. Напишите программу, которая составит список простых делителей числа N. (1 - составное число)


def simple_div(number):
    result = []
    for i in range(2, number + 1):
        if not number % i:
            result.append(i)
    return result

def main():
    input_number = int(input('Введите число - '))
    print(f'Простые делители {input_number} - {simple_div(input_number)}')

if __name__ == "__main__":
    main()