import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def del_info():
    # Удалить информацию из словаря.

    # Подменюшка внутри меню 4.
    print('*' * 47)
    print('[ Вы находитесь в меню 4, удаление информации из базы данных ]')
    print('[ Внимание! Ввод параметров чувствителен к регистру ]')
    print('1. Удалить запись полностью, или')  # value1.
    print('2. только конкретный параметр?')  # value2.
    print('*' * 47)

    # Приглашение к выбору варианта меню выше.
    value = int(input('> Выберите вариант:~$ '))

    if (value == 1):  # Снос всего ключа разом.
        print('[ Вы находитесь в меню 4.1, полное удаление записи из БД ]')
        print('[ Внимание! Данная опция полностью удалит запись из БД! ]')
        name = input('Введите имя сотрудника:~$ ')
        if name in main_dict.agents:  # <-- ВОТ ЗДЕСЬ [name] НЕ НАДО!!! Если добавить, работать НЕ БУДЕТ!!!
            del main_dict.agents[name]  # Сносит весь ключ и всё его содержимое!
            # agents.pop(name) # Аналогично предыдущей команде.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.agents)
        else:
            print('Сотрудник с таким именем не найден.')

    if (value == 2):  # Снос параметров внутри ключа.

        # Подменюшка, находящаяся внутри параметра 2.
        print('*' * 62)
        print('[ Вы находитесь в меню 4.2, удаление параметров из записи сотрудника ]')
        print('[ Какой параметр сотрудника необходимо удалить? ]')
        print('1. Телефон.')  # value1.
        print('2. e-mail.')  # value2.
        print('3. Должность.')  # value3.
        print('4. Офис.')  # value4.
        print('5. Skype.')  # value5.
        print('*' * 62)

        # Приглашение к выбору варианта меню выше.
        value = int(input('> Выберите параметр выше (введите от 1 до 5):~$ '))

        if (value == 1):  # Если выбрана кнопка 1 - Телефон.
            name = input('Введите имя сотрудника:~$ ')
            main_dict.agents[name].pop('Телефон')  # Удаляет телефон.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.agents)

        if (value == 2):  # Если выбрана кнопка 2 - e-mail.
            name = input('Введите имя сотрудника:~$ ')
            main_dict.agents[name].pop('e-mail')  # Удаляет e-mail.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.agents)

        if (value == 3):  # Если выбрана кнопка 3 - Должность.
            name = input('Введите имя сотрудника:~$ ')
            main_dict.agents[name].pop('Должность')  # Удаляет Должность.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.agents)

        if (value == 4):  # Если выбрана кнопка 4 - Офис.
            name = input('Введите имя сотрудника:~$ ')
            main_dict.agents[name].pop('Офис')  # Удаляет Офис.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.agents)

        if (value == 5):  # Если выбрана кнопка 5 - Skype.
            name = input('Введите имя сотрудника:~$ ')
            main_dict.agents[name].pop('Skype')  # Удаляет Skype.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.agents)