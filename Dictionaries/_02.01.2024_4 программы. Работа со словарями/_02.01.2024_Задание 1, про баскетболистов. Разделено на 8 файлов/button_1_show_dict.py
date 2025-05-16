import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def show_dict():
# Посмотреть словарь.
            printer = pprint.PrettyPrinter(width=100, indent=1) # Заводим переменную для хранения параметров pprint-a.
            # indent - это отступ слева, width - ширина. Переменную надо подкидывать вместе с принтом в каждый пункт меню.
            printer.pprint(main_dict.basketball_gamers) # Принтуем словарь через связку: переменная.библиотека.