def print_operation_table(operation, num_rows=9, num_columns=9):
    print('Полная таблица от 1 до искомого значения')
    for i in range(1, num_rows+1):
        print(*[operation(i,j) for j in range(1, num_columns+1)], sep='\t')
    return operation(num_rows,num_columns)

def main():
    row = int(input('Введи строку элемента - '))
    column = int(input('Введи столбец элемента - '))
    print(f'Искомый елемент - {print_operation_table(lambda x, y: x * y, row, column)}')

if __name__ == "__main__":
    main()