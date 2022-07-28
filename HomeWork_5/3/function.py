def encrypt(string):
    result = ''
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        elif count == 1:
            result += string[i]
        else:
            result += str(count) + string[i]
            count = 1
    if string[len(string) - 1] == string[len(string) - 2]:
        result += str(count) + string[len(string) - 2]
    else:
        result += string[len(string) - 1]
    return result

def decoder(string):
    result = ''
    count = ''
    for i in range(len(string)):
        if str(string[i]).isdigit():
            count += string[i]
        elif count == '':
            result += string[i]
        else:
            result += string[i] * int(count)
            count = ''
    return result