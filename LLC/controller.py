import model
import view
from prettytable import PrettyTable
import time


def init():
    global full_table
    model.tableFull()
    menuSelectOption()



def getPrintDict(dictName):
    menu = ''.join(f'{key} - {value}\n' for key, value in dictName.items())
    view.showInfo('white', f'{menu}')



def menuSelectOption():
    global full_table
    model.tableFull()
    actionMenu = {
        1: 'Получить полный список сотрудников',
        2: 'Получить выборочный список сотрудников',
        3: 'Редактировать данные сотрудника',
        4: 'Завести нового сотрудника',
        5: 'Удалить сотрудника',
        0: 'ВЫХОД'
    }
    action = {
        1: model.getAllStaff,
        2: model.sortStaff,
        3: model.editStaff,
        4: model.addStaff,
        5: model.deleteStaff,
        0: exit
    }
    view.showInfo('invert', f'\nВыберите действие:\n\n'.upper())
    getPrintDict(actionMenu)
    choice = view.inputInt('Выберите пункт меню: ')
    run = action.get(choice)
    if run:
        run()
    else:
        view.showInfo('red', f'Недопустимый выбор {choice}. Попробуйте снова!')
    if choice == 1:
        time.sleep(5)
        menuSelectOption()
    elif choice == 2:
        time.sleep(5)
        menuSelectOption()
    elif choice == 3:
        time.sleep(5)
        menuSelectOption()
    elif choice == 4:
        time.sleep(5)
        menuSelectOption()
    elif choice == 5:
        time.sleep(5)
        menuSelectOption()