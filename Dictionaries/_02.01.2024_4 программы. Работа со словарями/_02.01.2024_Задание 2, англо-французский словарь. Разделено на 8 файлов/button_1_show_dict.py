import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def show_dict():
# Посмотреть словарь.

    print('', '[eng] : [french]')  # Просто надпись над словарём, чтобы понимать где какое слово.
    printer = pprint.PrettyPrinter(width=100, indent=1)  # Заводим переменную для хранения параметров pprint-a.
    printer.pprint(main_dict.words)  # Принтуем словарь через связку: переменная.библиотека.