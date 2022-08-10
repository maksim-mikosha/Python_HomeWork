# Все равны, как на подбор

def same_by(operation, value):
    return all(not operation(i) for i in value)

def main():
    count_numbers = input('Введите количество чисел: ')
    if count_numbers:
        count_numbers = int(count_numbers)
        print('Введите числа: ')
        numbers = list()
        for i in range(count_numbers):
            input_value = int(input())
            numbers.append(input_value)
        if same_by(lambda x: x % 2, numbers):
            print('Same')
        else:
            print('Different')
    else:
        print('Same')

if __name__ == "__main__":
    main()