import view
from prettytable import PrettyTable
import csv



def tableFull():
    global full_table
    full_table = PrettyTable(['ФИО', 'Возраст (лет)', 'Специализация', 'Отдел'])
    full_table.add_row(['Андреева Анна Андреевна', '25', 'Работа со стандартными клиентами', 'Фронт-офис'])
    full_table.add_row(['Иванова Инна Ивановна', '26', 'Работа со стандартными клиентами', 'Фронт-офис'])
    full_table.add_row(['Козлова Наталья Кирилловна', '29', 'Работа с VIP-клиентами', 'Фронт-офис'])
    full_table.add_row(['Степанова Надежда Ивановна', '24', 'Работа с заявками', 'Бэк-офис'])
    full_table.add_row(['Тимербаева Альбина Талгатовна', '25', 'Работа с VIP-заявками', 'Бэк-офис'])
    full_table.add_row(['Петрова Ольга Петровна', '30', 'Руководитель', 'Администрация'])
    full_table.add_row(['Семенова Эльза Анатольевна', '35', 'Главный бухгалтер', 'Администрация'])
    full_table.add_row(['Майорова Алина Сергеевна', '33', 'Начальник отдела кадров', 'Администрация'])
    full_table.add_autoindex('ID')
    full_table.align['ФИО'] = "l"
    full_table.align['Возраст (лет)'] = "l"
    full_table.align['Специализация'] = "l"
    full_table.align['Отдел'] = "l"
    return full_table

def getAllStaff():
    view.showInfo('blue', ' ОБЩИЙ СПИСОК СОТРУДНИКОВ: ')
    with open('table.csv', 'r', encoding='UTF8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            view.printAny(' '.join(row))


def sortStaff():
    global full_table
    tableFull()
    check_list = ['ID', 'ФИО', 'Возраст (лет)', 'Специализация', 'Отдел']
    while True:
        try:
            to_print = view.inputStr('Введите через пробел столбцы для отображения: ').split()
            for i in to_print:
                if i not in check_list:
                    raise ValueError
        except ValueError:
            view.showInfo('red', 'ОШИБКА! ВВЕДИТЕ НАЗВАНИЯ СТОЛБЦОВ КОРРЕКТНО!')
            continue
        new_table = full_table.get_string(fields = to_print)
        view.showInfo('green', 'ПОЛУЧЕННЫЙ СПИСОК: ')
        view.printAny(new_table)
        break
    


def editStaff():
    global full_table
    view.showInfo('invert', '\nрежим редактирования данных\n\n'.upper())
    view.printAny(tableFull())
    while True:
        try:
            to_edit = str(view.inputInt('Введите ID сотрудника для изменения данных: '))
            if to_edit not in full_table.get_string(fields=['ID']):
                raise ValueError
        except ValueError:
            view.showInfo('red', 'ОШИБКА! ВВЕДИТЕ КОРРЕКТНЫЙ ID!')
            continue
        new_row = full_table.get_string(start = int(to_edit) - 1, end = int(to_edit))
        view.printAny(new_row)
        full_table.del_row(int(to_edit) - 1)
        new_row = view.getInfo()
        full_table.add_row(new_row)
        exportTable(full_table)
        view.showInfo('green', 'Данные сотрудника успешно изменены!')
        view.printAny(full_table)
        break



def addStaff():
    global full_table
    view.printAny(tableFull())
    view.showInfo('invert', '\nрежим добавления нового сотрудника\n\n'.upper())
    new_row = view.getInfo()
    full_table.add_row(new_row)
    exportTable(full_table)
    view.showInfo('green', 'Сотрудник успешно добавлен!')
    view.printAny(full_table)



def deleteStaff():
    global full_table
    view.showInfo('invert', '\nрежим удаления данных\n\n'.upper())
    view.printAny(tableFull())
    while True:
        try:
            to_delete = str(view.inputInt('Введите ID сотрудника для удаления: '))

            if to_delete not in full_table.get_string(fields=['ID']):
                raise ValueError
        except ValueError:
            view.showInfo('red', 'ОШИБКА! ВВЕДИТЕ КОРРЕКТНЫЙ ID!')
            continue
        full_table.del_row(int(to_delete) - 1)
        exportTable(full_table)
        view.showInfo('green', 'Сотрудник успешно удален!')
        view.printAny(full_table)
        break

    

def exportTable(table):
    with open('table.csv', 'w', encoding='UTF8') as f:
        f.write(str(table))


def importTable():
        with open('table.csv', 'r', encoding='UTF8', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(*row)