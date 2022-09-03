def check_gorizontal(list):
    value = ['O', 'X']
    for i in value:
        if i in str(list[0]) and i in str(list[1]) and i in str(list[2]):
            return True
        elif i in str(list[3]) and i in str(list[4]) and i in str(list[5]):
            return True
        elif i in str(list[6]) and i in str(list[7]) and i in str(list[8]):
            return True
    return False

def check_vertical(list):
    value = ['O', 'X']
    for i in value:
        if i in str(list[0]) and i in str(list[3]) and i in str(list[6]):
            return True
        elif i in str(list[1]) and i in str(list[4]) and i in str(list[7]):
            return True
        elif i in str(list[2]) and i in str(list[5]) and i in str(list[8]):
            return True
    return False

def check_diagonal(list):
    value = ['O', 'X']
    for i in value:
        if i in str(list[0]) and i in str(list[4]) and i in str(list[8]):
            return True
        elif i in str(list[6]) and i in str(list[4]) and i in str(list[2]):
            return True
    return False

def check_table(list):
    if 0 in list: return False
    return True