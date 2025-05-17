import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def del_info():
#  Удалить информацию о произведении.

    # Подменюшка внутри меню 4.
    print('*' * 47)
    print('[ Вы находитесь в меню 4, удаление произведения из библиотеки ]')
    print('[ Внимание! Ввод параметров чувствителен к регистру ]')
    print('1. Удалить произведение полностью, или')  # value1.
    print('2. только конкретный параметр?')  # value2.
    print('*' * 47)

    # Приглашение к выбору варианта меню выше.
    value = int(input('> Выберите вариант:~$ '))

    if (value == 1):  # Снос всего ключа разом.
        print('[ Вы находитесь в меню 4.1, полное удаление произведения ]')
        print('[ Внимание! Данная опция полностью удалит произведение из библиотеки ]')
        name = input('Введите название произведения:~$ ')
        if name in main_dict.books:  # <-- ВОТ ЗДЕСЬ [name] НЕ НАДО!!! Если добавить, работать НЕ БУДЕТ!!!
            del main_dict.books[name]  # Сносит весь ключ и всё его содержимое!
            # books.pop(name) # Аналогично предыдущей команде.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.books)
        else:
            print('Произведение с таким названием не найдено.')

    if (value == 2):  # Снос параметров внутри ключа.

        # Подменюшка, находящаяся внутри параметра 2.
        print('*' * 62)
        print('[ Вы находитесь в меню 4.2, удаление параметров из произведения ]')
        print('[ Какой параметр необходимо удалить? ]')
        print('1. Автор.')  # value1.
        print('2. Жанр.')  # value2.
        print('3. Год выпуска.')  # value3.
        print('4. Количество страниц.')  # value4.
        print('5. Издательство.')  # value5.
        print('*' * 62)

        # Приглашение к выбору варианта меню выше.
        value = int(input('> Выберите параметр выше (введите от 1 до 5):~$ '))

        if (value == 1):  # Если выбрана кнопка 1 - Название произведения.
            name = input('Введите название произведения:~$ ')
            main_dict.books[name].pop('Автор')  # Удаляет Автор.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.books)

        if (value == 2):  # Если выбрана кнопка 2 - Жанр.
            name = input('Введите название произведения:~$ ')
            main_dict.books[name].pop('Жанр')  # Удаляет Жанр.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.books)

        if (value == 3):  # Если выбрана кнопка 3 - Год выпуска.
            name = input('Введите название произведения:~$ ')
            main_dict.books[name].pop('Год выпуска')  # Удаляет Год выпуска.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.books)

        if (value == 4):  # Если выбрана кнопка 4 - Количество страниц.
            name = input('Введите название произведения:~$ ')
            main_dict.books[name].pop('Количество страниц')  # Удаляет Количество страниц.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.books)

        if (value == 5):  # Если выбрана кнопка 5 - Издательство.
            name = input('Введите название произведения:~$ ')
            main_dict.books[name].pop('Издательство')  # Удаляет Издательство.
            print('Запись удалена!')
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.books)