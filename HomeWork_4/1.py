# Вычислить число Pi c заданной точностью d


def count_pi(number):
    result = 0
    for i in range(number + 1):
        result += (1 / 16 ** i)*((4 / (8 * i + 1))-(2 / (8 * i + 4))-(1 / (8 * i + 5))-(1 / (8 * i + 6)))
    return result

def main():
    input_number = int(input('Введите желаемую точность вычисления - '))
    print(f'Число Pi с точностью {input_number} - {str(count_pi(input_number))[0:input_number+2]}')

if __name__ == "__main__":
    main()