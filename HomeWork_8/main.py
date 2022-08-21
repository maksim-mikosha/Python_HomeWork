'''
Создать информационную систему позволяющую работать с сотрудниками
некой компании \ студентами вуза \ учениками школы
'''
def reading_file_to_dict(number_file, database):
    with open(f'Python_HomeWork\HomeWork_8\{number_file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(';')))
        return database

def print_phones_by_type(type, database, db):
    phone = [i for i in database[db['phone']] if type in i[3]]
    for i in range(len(phone)):
        for j in range(len(database[1])):
            if phone[i][1] == database[1][j][0]:
                print(database[1][j][1] + ' ' + database[1][j][2] + ' ' + phone[i][2])
            
def print_phones_by_name(surname, database, db):
    id = [i for i in database[db['human']] if surname in i[2]][0]
    phone = [i for i in database[db['phone']] if id[0] == i[1]]
    print(*[i[2] + '\t' for i in phone])

def main():
    database = {}
    reading_file_to_dict(1,database)
    reading_file_to_dict(2,database)
    db = {'human': 1, 'phone': 2}
    print('Вот что я могу:',
          '1 - Поиск номера телефона по фамилии',
          '2 - Поиск по типу телефона')
    input_comand = int(input('Введи номер команды - '))
    if input_comand == 1:
        inpit_surname = input('Введи фамилию - ')
        try:
            print(f'Вот что нашел по фамилии - {inpit_surname}')
            print_phones_by_name(inpit_surname, database, db)
        except:
            print('Хмм.. У меня нет информации по данной фамилии')
    elif input_comand == 2:
        inpit_phone_type = input('Введи тип телефонного номера (Private/Work) - ')
        try:
            print(f'Вот что нашел по типу - {inpit_phone_type}')
            print_phones_by_type(inpit_phone_type, database, db)
        except:
            print('Что-то пошло не так!')
    else:
        print('Эх ты! Уже и команду ввести правильно не можешь)')

if __name__ == "__main__":
    main()