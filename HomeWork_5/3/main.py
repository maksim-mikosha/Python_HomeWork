# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

import function

def main():
    input_value = input('Что шифруем? Ввод - ')
    print(f'Вот что получилось - {function.encrypt(input_value)}')
    print(f'Теперь расшифруем. Вуаля - {function.decoder(function.encrypt(input_value))}')
    
if __name__ == "__main__":
    main()