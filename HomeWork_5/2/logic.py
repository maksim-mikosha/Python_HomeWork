def value_for_check():
    value_for_check = ['O', 'X']
    return value_for_check

def check_gorizontal(list):
    value = value_for_check()
    for i in value:
        if i in str(list[3]) and i in str(list[4]) and i in str(list[5]):
            return True
        elif i in str(list[9]) and i in str(list[10]) and i in str(list[11]):
            return True
        elif i in str(list[15]) and i in str(list[16]) and i in str(list[17]):
            return True
    return False
    
def check_vertical(list):
    value = value_for_check()
    for i in value:
        if i in str(list[3]) and i in str(list[9]) and i in str(list[15]):
            return True
        elif i in str(list[4]) and i in str(list[10]) and i in str(list[16]):
            return True
        elif i in str(list[5]) and i in str(list[11]) and i in str(list[17]):
            return True
    return False

def check_diagonal(list):
    value = value_for_check()
    for i in value:
        if i in str(list[3]) and i in str(list[10]) and i in str(list[17]):
            return True
        elif i in str(list[5]) and i in str(list[10]) and i in str(list[15]):
            return True
    return False