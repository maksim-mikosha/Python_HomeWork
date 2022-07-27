# Создайте программу для игры в ""Крестики-нолики"".

import ui, logic, move, logic_player


def main():
    print('Крестики-нолики или слабо?)')
    input_move = 0
    players = logic_player.who_first()
    desk = ui.create_desk()
    print(ui.view(desk))
    while not (logic.check_gorizontal(desk) or logic.check_vertical(desk) or logic.check_diagonal(desk)):
        if players['player'] == 1:
            print('Ходит игрок')
            input_move = int(input(f'\nВот доска, выбирай. Я выбираю - '))
            print(ui.view(move.move_player(desk, input_move, 'X')))
            players = logic_player.change_player(players)
        else:
            print('Ходит бот')
            print(ui.view(move.move_bot(desk, 'O')))
            players = logic_player.change_player(players)
    
    if players['player'] == 0:
        print('Конец игры. Победил игрок!')
    else:
        print('Конец игры. Победил бот(')

if __name__ == "__main__":
    main()