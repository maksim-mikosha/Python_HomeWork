# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


def number_to_bin(number):
    result = list()
    while number > 1:
        result.append(number % 2)
        number = number // 2
    else:
        result.append(number)
    result.reverse()
    return result

def main():
    input_number = int(input('Введите число - '))
    
    print(f'Число {input_number} в двоичной системе {number_to_bin(input_number)}')

if __name__ == "__main__":
    main()