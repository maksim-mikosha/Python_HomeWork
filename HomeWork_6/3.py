# Пам-парам парам-пам парам

def check(text):
    sets = set()
    for i in text:
        count = 0
        for j in i:
            if j in 'ауоыиэяюёе':
                count += 1
        sets.add(count)
    if len(sets) == 1:
        return 'yes'
    return 'no'


def main():
    text = input('Введите текст разделяя фразы пробелами ').split()
    print(check(text))

if __name__ == "__main__":
    main()