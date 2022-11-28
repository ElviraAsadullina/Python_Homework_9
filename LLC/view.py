def showInfo(color=None, text=None):
    if color == 'white':
        return print('\33[1m' + text + '\033[0m')
    elif color == 'red':
        return print('\33[31m' + text + '\033[0m')
    elif color == 'blue':
        return print('\33[34m' + text + '\033[0m')
    elif color == 'yellow':
        return print('\33[93m' + text + '\033[0m')
    elif color == 'green':
        return print('\33[92m' + text + '\033[0m')
    elif color == 'invert':
        return print('\33[7m' + text + '\033[0m')

def inputInt(text: int):
    while True:
        try:
            number = int(input(text))
            return number
        except:
            showInfo('red', 'Ошибка! Введите целое число!')

def inputStr(text):
    while True:
        try:
            string = input(text)
            return string
        except:
            showInfo('red', 'Ошибка! Введите слово!')

def printAny(func):
    print(func)

def getInfo():
    ID = input('ID сотрудника: ')
    name = input('ФИО сотрудника: ')
    age = input('Возраст сотрудника: ')
    speciality = input('Специализация сотрудника: ')
    department = input('Отдел сотрудника: ')
    new_data = [ID, name, age, speciality, department]
    return new_data

