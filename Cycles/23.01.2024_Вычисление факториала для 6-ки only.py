﻿# Задача: необходимо с помощью цикла for найти факториал 6-и.
# Также, с помощью операторов ветвлений if / elif необходимо сделать
# обработку ошибок, если пользователь, например, ввёл число меньше,
# или больше 6-и.

# Что такое факториал? Это произведение всех натуральных чисел от 1 до данного числа.

# Запускаем бесконечный цикл while.
while(True):
    try:

        # Приглашение к вводу команды.
        value1 = int(input('Вычисление факториала для 6:~$ '))

        # Переменная для вычисления факториала конкретно для шестёрки.
        factorial = 1*2*3*4*5

        # Запускаем цикл for.
        # Итерации от 1 до числа, введённого пользователем,
        # -4, в данном случае, нужен для того, чтобы не выводить весь диапазон,
        # а показать только одно последнее значение.
        for i in range(1, value1-4):

            # Если пользователь ввёл больше 6, тогда завершаем.
            if value1 > 6:
                break

            # Если пользователь ввёл меньше 6, тогда опять завершаем.
            elif value1 < 6:
                break

            # Если пользователь ввёл конкретно 6, тогда принтуем результат факториала шестёрки.
            elif value1 == 6:
                print('Факториал 6 равен:', value1 * factorial)

    except: continue