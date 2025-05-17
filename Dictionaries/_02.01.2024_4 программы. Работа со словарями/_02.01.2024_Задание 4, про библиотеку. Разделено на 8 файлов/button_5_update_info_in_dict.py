import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def update_info():
# Обновление информации в библиотеке (в словаре).

    print('[ Вы находитесь в меню 5, обновление информации о произведении ]')
    print('[ Внимание! Ввод данных чувствителен к регистру ]')
    name = input('Введите название произведения:~$ ')
    if name in main_dict.books:
        author = input('Введите имя автора:~$ ')
        genre = input('Введите жанр:~$ ')
        date = input('Введите год выпуска:~$ ')
        papers = input('Введите количество страниц:~$ ')
        publishing_house = input('Введите название издательства:~$ ')
        print('Информация в библиотеке обновлена!')  # Информация обновлена для меню 5.
        main_dict.books[name] = {'Автор: ' + author, 'Жанр: ' + genre, 'Год выпуска: ' + date, 'Количество страниц: ' + papers,
                       'Издательство: ' + publishing_house}
        printer = pprint.PrettyPrinter(width=100, indent=1)
        printer.pprint(main_dict.books)
    else:
        print('Неверное название произведения!')
        print('Нельзя обновить данные у несуществующей записи.')