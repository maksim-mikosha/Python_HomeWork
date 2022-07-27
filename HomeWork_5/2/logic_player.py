from random import randint

def who_first():
    dictionary = {"player": 0, "bot": 0}
    dictionary['player'] = randint(0, 100)
    dictionary['bot'] = randint(0, 100)
    if dictionary['player'] > dictionary['bot']:
        dictionary['player'] = 1
        dictionary['bot'] = 0
    else:
        dictionary['bot'] = 1
        dictionary['player'] = 0
    return dictionary

def change_player(dictionary):
    if dictionary['player'] > dictionary['bot']:
        dictionary['player'] = 0
        dictionary['bot'] = 1
    else:
        dictionary['bot'] = 0
        dictionary['player'] = 1
    return dictionary