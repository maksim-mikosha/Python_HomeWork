# Вклад в банке составляет X рублей. 
# Ежегодно он увеличивается на P процентов, после чего дробная часть копеек отбрасывается.
# Требуется определить: через сколько лет вклад составит не менее Y рублей.


def deposit_count(first, persent, finish):
    year_count = 0
    while first <= finish:
        first += first * (persent / 100)
        first = round(first, 0)
        year_count += 1
    return year_count

def main():
    first_dep = int(input('Введите первоначальный сумму - '))
    persent = int(input('Введите проценты по вкладу - '))
    finish_dep = int(input('Введите желаемую сумму - '))

    print(f'Для достижения цели в {finish_dep} рублей нужно {deposit_count(first_dep, persent, finish_dep)} лет')

if __name__ == "__main__":
    main()