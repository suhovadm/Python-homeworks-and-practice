﻿# Задача: напишите программу, использующую вложенный цикл for.
# Пользователь вводит некий диапазон чисел, например от 1 до 5.
# Для каждого числа выводится таблица умножения от 1 до 10, т.е.
# 1 x 1, 1 x 2, 1 x 3 и так до 10, дальше 2 x 1, 2 x 2, 2 x 3 и так до 10,
# и так весь диапазон до 5-и.

# Добавьте в скрипт форматирование, чтобы диапазоны таблиц умножения
# выводились не в столбик, а в строчку.

# Запускаем бесконечный цикл while.
while(True):
    try:

        # Приглашение к вводу команд.
        value1 = int(input('Введите первое число диапазона таблицы умножения:~$ '))
        value2 = int(input('Введите второе число диапазона таблицы умножения:~$ '))

        # Запускаем цикл for с диапазоном чисел, введённых пользователем по второе число включительно (+1).
        for count1 in range(value1, value2+1):

            # Второй диапазон определяет диапазон умножения, то есть, числа будут умножаться от х1 до х10.
            for count2 in range(1, 11):

                # Переменная result хранит результат умножения первого каунта на второй.
                result = count1 * count2

                # Принтуем результат через f-строку.
                # Кидаем в f-строку значения count1 умноженный на count2 = result.
                # Добавляем end='\t' для вывода значений в строчку, а не в столбик.
                print(f'{count1} * {count2} = {result}',end='\t')

            # Добавляем ещё один '\n' для того чтобы значения выводились через строчку, а не слитно.
            print('\n')

    except: continue