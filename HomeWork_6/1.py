# Мимикрия

def main():
    values = [1, 23, 42, 543 ,67, 'adf', 'asd', 34, 'qwerty']
    transformed_values = list(map(lambda x: x, values))
    if values == transformed_values:
        print('Ok')
    else:
        print('Fail')

if __name__ == "__main__":
    main()