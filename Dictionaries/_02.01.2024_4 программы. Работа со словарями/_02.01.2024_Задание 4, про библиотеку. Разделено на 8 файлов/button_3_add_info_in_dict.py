import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def add_info():
# Добавить новое произведение, или обновить информацию о существующем.

    print('[ Вы находитесь в меню 3, добавление нового произведения ]')
    print('[ Если ввести уже существующее название произведения, информация о нём будет обновлена ]')
    name = input('Введите название произведения:~$ ')
    author = input('Введите имя автора:~$ ')
    genre = input('Введите жанр:~$ ')
    date = input('Введите год выпуска:~$ ')
    papers = input('Введите количество страниц:~$ ')
    publishing_house = input('Введите название издательства:~$ ')
    main_dict.books[name] = {'Автор: ' + author, 'Жанр: ' + genre, 'Год выпуска: ' + date, 'Количество страниц: ' + papers,
                   'Издательство: ' + publishing_house}
    print('Информация в библиотеке обновлена!')  # Информация обновлена для меню 3.
    printer = pprint.PrettyPrinter(width=120, indent=1)
    printer.pprint(main_dict.books)  # В данном случае, выводит всю базу данных (словарь).