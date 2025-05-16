import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def del_info():
# Удалить информацию о баскетболисте.

    # Подменюшка внутри меню 4.
    print('*'*47)
    print('[ Вы находитесь в меню 4, удаление информации ]')
    print('[ Внимание! Ввод параметров чувствителен к регистру ]')
    print('1. Снести весь ключ, или') # value1.
    print('2. конкретный параметр?') # value2.
    print('*'*47)

    # Приглашение к вводу команды.
    value = int(input('> к0г0? '))

    if (value == 1): # Снос всего ключа разом.
        print('[ Вы находитесь в меню 4.1, полное удаление ключа из словаря ]')
        print('[ Внимание! Данная опция снесёт весь ключ и всё его содержимое! ]')
        name = input('Введите имя игрока (например, Magic Johnson):~$ ')
        if name in main_dict.basketball_gamers: # <-- ВОТ ЗДЕСЬ [name] НЕ НАДО!!! Если добавить, работать НЕ БУДЕТ!!!
            del main_dict.basketball_gamers[name] # Сносит весь ключ и всё его содержимое!
            # basketball_gamers.pop(name) # Аналогично предыдущей команде.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.basketball_gamers)
        else:
            print('Игрок с таким именем не найден.')

    if (value == 2): # Снос параметров внутри ключа.

        # Подменюшка, находящаяся внутри параметра 2.
        print('*' * 62)
        print('[ Вы находитесь в меню 4.2, удаление параметров внутри ключа ]')
        print('1. Рост.') # value1.
        print('2. Номер игрока.') # value2.
        print('3. Команда.') # value3.
        print('*' * 62)

        # Приглашение к вводу команды.
        value = int(input('> Выберите параметр выше (введите от 1 до 3):~$ '))

        if (value == 1): # Если выбрана кнопка 1 - Рост.
            name = input('Введите имя игрока (например, Michael Jordan):~$ ')
            main_dict.basketball_gamers[name].pop('Рост') # Удаляет рост игрока. Ключ и др. параметры не трогает.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.basketball_gamers)

        if (value == 2): # Если выбрана кнопка 2 - Номер игрока.
            name = input('Введите имя игрока (например, Michael Jordan):~$ ')
            main_dict.basketball_gamers[name].pop('Номер игрока') # Удаляет номер игрока.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.basketball_gamers)

        if (value == 3): # Если выбрана кнопка 3 - Команда.
            name = input('Введите имя игрока (например, Michael Jordan):~$ ')
            main_dict.basketball_gamers[name].pop('Команда') # Удаляет команду.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.basketball_gamers)