import csv

def fill_first_dict(dict):
    dict = {"0" : ("First name", "Second name", "Number", "Note"),
            "1" : ("Ivan", "Petrov", "4952578645", "Work number"),
            "2" : ("Sergey", "Vasechkin", "4612358476", "Work number"),
            "3" : ("Maksim", "Popov", "9782536741", "Privat number")}
    return dict

def add_to_file(list):
    pass

def import_to_line(dict):
    with open("Python_HomeWork\HomeWork_7\import-variant1.csv", "w") as file:
        for key in dict:
            if int(key) > 0:
                file.write('; '.join(str(dict[key]).split(',')))
                file.write('\n')

def import_by_line(dict):
    with open("Python_HomeWork\HomeWork_7\import-variant2.csv", "w") as file:
        for key in dict:
            if int(key) > 0:
                for value in dict[key]:
                    file.write(' '.join(str(value).split(',')))
                    file.write('\n')
            file.write('-' * 15 + '\n')