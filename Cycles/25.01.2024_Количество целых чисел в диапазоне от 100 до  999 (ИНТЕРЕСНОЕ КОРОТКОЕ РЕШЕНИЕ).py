﻿# Задача: подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры.
# Для реализации функционала используйте цикл for.
# Не используйте цикл while(True) в обвязке основного кода, так как,
# если его добавить, будет бесконечный вывод одного и того же.

# *** В данном случае использован while(True) с брейком, который тут
# же прерывает его после первого же выполнения. В этом нет особого смысла, это сделано просто для теста.

# Вариант 2. Интересное решение в одну строку сразу в Принте.

# Запускаем цикл while(True).
while(True):
    
        # range - генерирует числа от 100 до 999 включительно.
        # str(i) - преобразует число в строку.
        # set(str(i)) - создаёт множество уникальных цифр этого числа.
        # len(set(str(i))) - определяет количество уникальных цифр в числе.
        # Выражение len(set(str(i))) < 3 - проверяет, есть ли в числе повторяющиеся цифры.
        # Если уникальных цифр меньше 3, значит есть хотя бы повторяющиеся цифры (поскольку в трёхзначном
        # числе максимум 3 цифры).
        # Для трёхзначных чисел, у которых все цифры разные, len(set(str(i))) будет равно 3.
        # Поэтому условие < 3 истинно для чисел, у которых есть хотя бы одна повторяющаяся цифра.
        # sum(...) - суммирует количество таких чисел.

        print('Количество одинаковых чисел в диапазоне от 100 до 999 =', sum(len(set(str(i)))
                                                                             < 3 for i in range(100, 999+1)))
        break # Прерывает вывод надписи после первого раза.

# 100 - 999 - трёхзначный диапазон, поэтому i < 3.
# sum - суммирует цифры трёхзначного диапазона.
# len - длина.
# set - множество.
# str - строковый тип данных в Юникоде.
