# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def fibonachi(number):
    result = list([0, 1])
    for i in range(2, number + 1):
        result.append(result[i - 2] + result[i - 1])
    return result
    
def negafibonachi(list, number):
    result = list
    result.reverse()
    result.append(1)
    for i in range(1, number):
        result.append(- result[-1] + result[-2])
    result.reverse()
    return result
    
def main():
    input_number = int(input('Введите число - '))
    
    print(f'Негафибоначи - {negafibonachi(fibonachi(input_number), input_number)}')

if __name__ == "__main__":
    main()