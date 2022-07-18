# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def main():
    input_string = input('Введите список из чисел разделяя пробелами - ').split(' ')
    result = list()
    result.append(int(input_string[0]) * int(input_string[len(input_string) - 1]))

    for i in range(1, len(input_string)):
        if i <= (len(input_string) - 1) / 2:
            result.append(int(input_string[i]) * int(input_string[-i - 1]))
        else:
            break
    print(f'Произведение пар чисел - {result}')

if __name__ == "__main__":
    main()