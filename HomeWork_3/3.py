# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


def main():
    input_string = input('Введите список из вещественных чисел разделяя их пробелами - ').split(' ')
    float_list = list()
    for i in range(len(input_string)):
        float_list.append(float(input_string[i]))
        float_list[i] = round(float_list[i] - int(float_list[i]), 10)

    print(f'Разница между максимальным и минимальным значением дробной части элементов - {round(max(float_list) - min(float_list), 10)}')

if __name__ == "__main__":
    main()