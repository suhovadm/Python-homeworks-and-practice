# Задача на геометрические фигуры.
# Пользователь вводит высоту и ширину.
# Нужно вывести пустой прямоугольник.
# По желанию: сделать перехват ошибок,
# чтобы пользователь мог вводить только цифры.

# Запускаем бесконечный цикл while.
while(True):
    try:

        # Приглашение к вводу команд.
        width = int(input('Введите ширину прямоугольника:~$ ')) # Ширина.
        height = int(input('Введите высоту прямоугольника:~$ ')) # Высота.

        # Переменная, обозначающая звёздочку, то есть, то из чего будет состоять прямоугольник.
        a = '*'
        # Умножаем переменную "a" на ширину. Получаем верхнюю крышку прямоугольника.
        print(a * width)

        # Запускаем цикл for. Высоту (height) - 1 берём из предыдущего скрипта.
        for i in range(height - 1):
             print(a, ' ' * (width - 2), a, sep='')

            # a - сначала выводим вертикальную полосу из звёздочек. Она получается из
            # переменной height (высота).
            # Далее, выводим пустоту внутри прямоугольника при помощи пробела ' '
            # Далее, умножаем всё это дело на ширину.
            # * (width - 2) - это подгон ширины пустоты внутри прямоугольника, аналогично предыдущему скрипту.
            # a - снова выводим вертикальную полосу из звёздочек. Она, опять таки,
            # получается из переменной height (высота).
            # sep='' - это внутренний отступ (символ) переменной а. В данном случае, пробел.

        print(a * width) # Умножаем переменную "а" на ширину. Получаем нижнюю крышку прямоугольника.

    except ValueError:
        print('Ошибка! Можно вводить только целочисленные значения.')
        continue

# break # выключен. Перезапускаем программу.
