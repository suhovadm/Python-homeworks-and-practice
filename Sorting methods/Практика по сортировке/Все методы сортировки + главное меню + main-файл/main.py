 # Упражнение на методы сортировки.
 # Реализуйте программу, которая предложит пользователю все методы сортировки
 # на выбор. Разделите код на несколько файлов для удобства, главное меню должно
 # быть в отдельном файле. У программы должна быть возможность выхода и обработка
 # ошибок, на тот случай, если пользователь выбрал не верный пункт меню.

from main_menu import main_menu

# Запускаем цикл while.
while (True):
    try:

        # Подтягиваем главное меню из файла main_menu.py
        main_menu()

        # Приглашение к выбору пунктов меню выше.
        # В данном случае выставлено int, потому что все пункты меню выставлены числами,
        # а не строчным значением через кавычки.
        menu = int(input('Выберите тип сортировки:~$ '))

        if (menu == 1):  # Кнопка 1, пузырьком.
            from bubble import *  # Подтягиваем скрипт из файла bubble.py
            continue

        elif (menu == 2):  # Кнопка 2, вставкой.
            from insertion import *  # Подтягиваем скрипт из файла insertion.py
            continue

        elif (menu == 3):  # Кнопка 3, слиянием.
            from merge import *  # Подтягиваем скрипт из файла merge.py
            continue

        elif (menu == 4):  # Кнопка 4, первая половина списка по убыванию, вторая - по возрастанию.
            from ubyv_vozrast import * # Подтягиваем скрипт из файла ubyv_vozrast.py
            continue

        elif (menu == 5): # Кнопка 5, частичная сортировка.
            from chast_sort import * # Подтягиваем скрипт из файла chast_sort.py
            continue

        elif (menu == 6): # Кнопка 6, сортировка встроенным методом Timsort.
            from Timsort import * # Подтягиваем скрипт из файла Timsort.py
            continue

        elif (menu == 7): # Кнопка 7, сортировка методом Хоара.
            from Hoar_method import * # Подтягиваем скрипт из файла Hoar_method.py
            continue

        elif (menu == 8): # Кнопка 8, сортировка методом Шелла.
            from Shell_method import * # Подтягиваем скрипт из файла Shell_method.py
            continue

        elif (menu == 9): # Кнопка 9, пирамидальная сортировка.
            from pyramid_method import * # Подтягиваем скрипт из файла pyramid_method.py
            continue

        elif (menu == 0): # Кнопка 0, выход из программы по нажатию кнопки "0".
            print('До новых встреч!')
            break

        # Перехват ошибок на тему того, что выбран неверный пункт меню.
        else:
            print('Ошибка! Извините, выбран неверный пункт меню.')

    # Перехват ошибок на тему того, что при выборе пункта меню пользователь ввёл не цифру.
    except ValueError:
        print('Ошибка! Извините, можно вводить только числовое значение.')
        continue