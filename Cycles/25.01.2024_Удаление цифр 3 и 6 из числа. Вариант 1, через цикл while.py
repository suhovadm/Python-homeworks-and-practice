﻿# Задача: напишите программу, которая выкидывает цифры 3 и 6 из целого числа. 
# То есть, пользователь вводит, например, 236, на экране остаётся только 2.
# Реализовать функционал нужно с помощью цикла while, или for.

# Вариант 1.

# Запускаем бесконечный цикл while.
while(True):
    try:

        # Приглашение к вводу команды.
        print('Введите любое целое число. Числа 3 и 6 удаляются.')
        value1 = int(input('Введите любое целое число:~$ '))

        # --- БЛОК 1. Переменные для хранения значений. ---
        result = 0 # Переменная для хранения итогового числа, которое будет выводиться.
        countinnumber = 0 # Счётчик позиции текущей обрабатываемой цифры в числе, начиная с нуля.

        # --- БЛОК 2. Обработчик. ---
        # В нашем случае, вложенный цикл. Проверяем, что вводимое пользователем число больше 0.
        # Весь цикл будет продолжаться до тех пор, пока value1 > 0, то есть пока есть цифры
        # для обработки.
        while value1 > 0:

            # Извлекаем последнюю цифру с помощью операции value1 % 10 и сохраняем в переменную num.
            num = value1 % 10

            # Теперь проверяем, равна ли эта цифра 3 или 6.
            # Если эта цифра не равна 3 и не равна 6, то ...
            if num != 3 and num != 6:

                # ... эта цифра прибавляется к результату result, но не просто как есть, а с учётом
                # её позиции в числе. Для этого цифра умножается на 10 в степени countinnumber и
                # прибавляется к result.
                # Это позволяет "собрать" число из цифр, расположенных в правильных разрядах.
                result = result + num * 10**countinnumber

                # <--------------------------------------
                # Возводим счётчик цифр внутри числа в 10-ю степень,
                # далее, перемножаем это с НЕ равно 3 и 6 и складываем с результатом.
                # Если откинуть переменную **countinnumber, или возведение в 10-ю степень,
                # числа будут просто перемножаться друг с другом, например, при вводе
                # 333777, покажет не 777, а 21.
                # При использовании * 10**countinnumber работает правильно! Без него - нет!

                # countinnumber увеличивается на 1, чтобы следующая цифра заняла правильную
                # позицию в итоговом числе.
                countinnumber = countinnumber + 1

            # value1 делится на 10 с помощью целочисленного деления // 10, чтобы удалить последнюю
            # обработанную цифру и перейти к следующей.
            value1 = value1 // 10

        print('\nРезультат без 3 и 6:',result,'\n')

    except: continue

# break # отключён. Зацикливаем программу.