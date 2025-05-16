import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def add_info():
# Добавить информацию в словарь.

    print('[ Вы находитесь в меню 3, добавление информации ]')
    print('[ Если ввести уже существующее слово, то информация о нём будет обновлена ]')
    key = input('Введите слово на английском языке (например, cat, dog, bear и т.д.):~$ ')
    parameter = input('И перевод на французский:~$ ')
    main_dict.words[key] = parameter
    # words - словарь
    # key - ключ
    # parameter - параметр ключа
    print('Информация в словаре обновлена!')
    print('', '[eng] : [french]')  # Просто надпись над словарём, чтобы понимать где какое слово.
    printer = pprint.PrettyPrinter(width=100, indent=1)
    printer.pprint(main_dict.words)