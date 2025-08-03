from load_dictionary import *
from get_translation_choice import *
from output_translation import *
import main_menu

# Объявляем main-овую функцию программы, которая содержит основной поток выполнения.
def main():

    # Задаём файл с выходными данными, т.е. наш OUT.txt
    output_file = 'OUT.txt'

    # Загружаем словари.
    # Вызывается функция load_dictionary() с указанными файлами, результат сохраняется
    # в переменные rus_to_eng и eng_to_rus.
    rus_to_eng, eng_to_rus = load_dictionary()

    # Подтягиваем функцию с главным меню из файла main_menu.py
    main_menu.menu()

    # Данная часть отвечает за взаимодействие с пользователем,
    # чтобы определить какое направление перевода он хочет выполнить.
    # Для этого, подтягиваем функцию get_translation_choice с аргументами rus_to_eng и eng_to_rus из
    # файла get_translation_choice.py
    # Аргумент rus_to_eng - это словарь переводов с русского на английский.
    # Аргумент eng_to_rus - это словарь переводов с английского на русский, т.е. обратка.

    # Возможно, данный while(True) избыточен, так как он же есть в файле get_translation_choice.py,
    # но всё работает :)
    while(True):
        translation_dict, direction = get_translation_choice(rus_to_eng, eng_to_rus)

        # Если пользователь отменил выбор, или произошла ошибка, функция get_translation_choice
        # возвращает None вместо словаря.
        if translation_dict is None:
            return

        # Подтягиваем функционал записи в файл OUT.txt из файла output_translation.py
        save_translation_to_file(output_file, translation_dict, direction)

# Запускаем программу с основной функции main().
if __name__ == "__main__":
    main()