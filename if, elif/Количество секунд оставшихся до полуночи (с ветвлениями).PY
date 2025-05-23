﻿# Задача: пользователь вводит количество секунд, прошедших с начала дня.
# Программа, на выбор, должна показать, сколько секунд, минут, или часов осталось до конца дня.
# При выполнении задачи нужно использовать операторы ветвлений.

# ---------------------------------------
# Количество секунд в сутках = 86400
# Количество минут в сутках = 1440
# Количество часов в сутках = 24
# ---------------------------------------
# Перевод секунд в минуты: 86400 /60
# Перевод секунд в часы: 86400 / 60 / 60
# ---------------------------------------

# Запускаем цикл.
while(True):
    try:

        # В данном случае, все три переменные переведены в секунды, обработчик закинут в print ниже.
        a1 = 86400 # Общее количество секунд в сутках.
        a2 = 86400 # Перевод секунд в минуты.
        a3 = 86400 # Перевод секунд в часы.

        # Первое поле для ввода пользователем.
        # В данном случае, он выводит количество секунд, которое прошло сначала дня.
        # float позволяет нам вводить дробные значения через точку.
        value = float(input('> Введите количество секунд, прошедшее сначала дня (слитно, через точку):~$ '))

        print('*' * 23)  # Первая звёздочка, умноженная в 23 раза. Сверху, над меню.
        print('> 1. Количество секунд.')  # Кнопка 1, value 1 ниже.
        print('> 2. Количество минут.')  # Кнопка 2, value 2 ниже.
        print('> 3. Количество часов.')  # Кнопка 3, value 3 ниже.
        print('*' * 23)  # Вторая звёздочка, уможенная в 23 раза. Снизу, под меню.

        # Второе поле для ввода пользователем.
        # Пункты меню работают только, если стоят НАД value, если закинуть
        # их под value, работать не будут.
        value1 = int(input('> Что хотим посмотреть, секунды, минуты, или часы? '))

        # Выбираем первый пункт print, количество секунд.
        if (value1 == 1):
            b1 = print('> Количество секунд, оставшихся до полуночи:', a1 - value, 'сек.')

        # Выбираем второй пункт print, количество минут.
        elif (value1 == 2):
            b2 = print('> Количество минут, оставшихся до полуночи:', (a2 - value) / 60, 'мин.')

        # Выбираем третий пункт print, количество часов.
        elif (value1 == 3):
            b3 = print('> Количество часов оставшихся до полуночи:', (a3 - value) / 60 / 60, 'час.')

    except:
        continue # Продолжаем. Если пользователь ввёл что-то не то вместо секунд в самом начале, сработает try / except.

#break # отключён. Зацикливаем программу.
