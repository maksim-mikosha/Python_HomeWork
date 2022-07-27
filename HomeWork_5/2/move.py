from random import randint


def move_player(desk, number, symbol):
    for i in range(len(desk)):
        if str(number) in str(desk[i]):
            temp_str = ''.join(map(str, desk[i])).split()
            temp_str[1] = symbol
            desk[i] = temp_str
            break
    return desk

def move_bot(desk, symbol):
    number = 0
    temp_str = ''.join(map(str, desk)).split()
    while not (str(number) in temp_str):
        number = randint(1,10)
    for i in range(len(desk)):
        if str(number) in str(desk[i]):
            temp_str = ''.join(map(str, desk[i])).split()
            temp_str[1] = symbol
            desk[i] = temp_str
            break
    return desk