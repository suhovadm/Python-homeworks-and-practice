# Задача: напишите итеративную (не рекурсивную) функцию для того, чтобы узнать,
# какое из четырёх введённых пользователем чисел больше других.

# Запускаем бесконечный цикл, чтобы программа не прерывалась.
while(True):
    try:

        # Определяем функцию для вывода максимального числа из четырёх.
        def maxnumber():

            # Делаем приглашение к вводу команд под каждое целое число.
            value1 = int(input('Введите первое число:~$ '))
            value2 = int(input('Введите второе число:~$ '))
            value3 = int(input('Введите третье число:~$ '))
            value4 = int(input('Введите четвёртое число:~$ '))

            # Проверяем, что value1 больше трёх других.
            if value1 > value2 and value1 > value3 and value1 > value4:
                print('Максимальное число:', value1)  # Принтуем value1.

            # Проверяем, что value2 больше трёх других.
            elif value2 > value1 and value2 > value3 and value2 > value4:
                print('Максимальное число:', value2)  # Принтуем value2.

            # Проверяем, что value3 больше трёх других.
            elif value3 > value1 and value3 > value2 and value3 > value4:
                print('Максимальное число:', value3)  # Принтуем value3.

            # Проверяем, что value4 больше трёх других.
            elif value4 > value1 and value4 > value2 and value4 > value3:
                print('Максимальное число:', value4)  # Принтуем value4.

        maxnumber()  # Запускаем функцию для вывода максимального числа из четырёх.

    except: continue