# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) (доп) Подумайте как наделить бота ""интеллектом""

from random import randint

    
def main():
    print('Хочешь сыграть в игру?! Начнём :)')
    player = randint(0, 100)
    bot = randint(0, 100)
    if player > bot:
        player = 1
        print('Начинает игрок')
        table = int(input('Введи начальное количество конфет - '))
        amount_in_round = int(input('Введи сколько можно взять конфет за один раз - '))
    else:
        bot = 1
        print('Начинает комп')
        table = randint(21, 101)                    # Из головы числа)
        print(f'Начальное количество конфет - {table}')
        amount_in_round = randint(1, 10)
        print(f'За один раз можно взять от 1 до {amount_in_round} конфет')
    
    while table > 0:
        if player == 1:
            print('-----------')
            print('Ход Игрока!')
            count_in_round = int(input('Игрок, введи сколько конфет берешь со стола - '))
            if 1 <= count_in_round <= amount_in_round:
                table -= count_in_round
                print(f'Игрок взял {count_in_round} конфет. На столе осталось {table} конфет')
                if table <= 0:
                    continue
                else:
                    player = 0
                    bot = 1
            else:
                print(f'Не тупи! За один раз можно взять от 1 до {amount_in_round} конфет')

        if bot == 1:
            print('-----------------------')
            print('Ход бездушной железяки)')
            count_in_round = randint(1, amount_in_round)
            table -= count_in_round
            print(f'Комп берет со стола {count_in_round} конфет. На столе осталось {table} конфет')
            if table <= 0:
                continue
            else:
                player = 1
                bot = 0

    if player == 1:
        print('******************')
        print(f'Победил игрок !!!')
    else:
        print('****************')
        print(f'Победил комп :(')

if __name__ == "__main__":
    main()