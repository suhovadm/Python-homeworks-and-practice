﻿# Задача: написать программу, которая сравнивает два числа.
# Если числа равны, пишет, что числа равны, если числа не
# равны, выводит их отсортированный список.
# Для реализации функционала нужно использовать операторы ветвлений.

# Запускаем бесконечный цикл while.
while(True):
    try:

        # Приглашение к вводу команд.
        # Приводим оба ввода к str, т.е. к строковому значению, чтобы можно было завести значения в список.
        value1 = str(input('> Введите первое число (можно дробное, через точку, или запятую):~$ '))
        value2 = str(input('> Введите второе число (можно дробное, через точку, или запятую):~$ '))

        # Загоняем первый и второй value в список!
        list1 = [value1, value2]

        # Определяем, равны числа между собой, или нет.
        # В данном случае, просто сравниваем первый value со вторым.
        # Если они равны, пишем, что числа равны.
        if value1 == value2:
            print('Числа равны.')

        # Если значение 1 не равно значению 2, то:
        elif value1 != value2:
            # Выводит просто обычный сортированный список с нашими значениями.
            print(sorted(list1))
            # Выводит тот же сортированный список с нашими значениями, через запятую, применяя метод
            # .join, чтобы убрать одинарные кавычки и квадратные скобки.
            print(', '.join(sorted(list1)))

    except: continue

# break # Выключен. Перезапускаем программу.