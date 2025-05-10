# Задача: пользователь вводит стоимость 1 игровой приставки, количество и процент скидки.
# В зависимости от выбора пользователя посчитать общую сумму заказа или стоимость 1
# приставки с учетом скидки.
# Для реализации функционала использовать операторы ветвлений if / elif.
# По желанию: разбить программу на несколько файлов для более читаемого кода.

import main_menu
import button_1
import button_2
import button_3
import button_4

# Запускаем бесконечный цикл while.
while(True):
    try:

        # Приглашение к вводу команд.
        value1 = float(input('> Введите стоимость консоли в рублях (можно через точку, без пробелов):~$ '))
        value2 = int(input('> Введите количество консолей (только целое число, без точек и запятых):~$ '))
        value3 = float(input('> Введите процент скидки на консоль (можно через точку, без пробелов):~$ '))

        # Выводим функцию с главным меню из файла main_menu.py
        main_menu.show_main_menu()

        # Приглашение к вводу команды, что конкретно нужно посчитать...
        choice = int(input('> Что нужно посчитать, общую сумму заказа, или стоимость 1 консоли? '))

        if choice == 1:
            button_1.show_obshaya_summa_zakaza(value1, value2)

        elif choice == 2:
            button_2.show_obshaya_summa_zakaza_so_skidkoi(value1, value2, value3)

        elif choice == 3:
            button_3.show_stoimost_1_consoli_without_skidka(value1, value2)

        elif choice == 4:
            button_4.show_stoimost_1_consoli_so_skidkoi(value1, value2, value3)

        else:
            print('Ошибка! Некорректный выбор. Пожалуйста, повторите попытку.')

    except: continue

# break # отклюён. Перезапускаем цикл while.