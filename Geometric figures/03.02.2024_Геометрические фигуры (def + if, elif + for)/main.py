import main_menu

import button1, button2, button3, button4, button5, button6, button7, button8, button9, button10

# Запускаем бесконечный цикл while.
while(True):
    try:

        # Подтягиваем главное меню.
        main_menu.menu()

        # Приглашение к выбору пунктов меню выше.
        value = int(input('Выберите геометрическую фигуру (от 1 до 10):~$ '))

        # value == 0. Кнопка 0. Выход из программы.
        if (value == 0):
            print('\nДо новых встреч.')
            break

        # value == 1. Кнопка 1. А. Правый верхний угол.
        # Кнопка 1. А. Правый верхний угол.
        elif (value == 1):
            button1.right_upper_angle()

        # value == 2. Кнопка 2. Б. Левый нижний угол.
        # Кнопка 2. Б. Левый нижний угол.
        elif (value == 2):
            button2.left_lower_angle()

        # value == 3. Кнопка 3. В. Верхний треугольник.
        # Кнопка 3. В. Верхний треугольник.
        elif (value == 3):
            button3.upper_triangle()

        # value == 4. Кнопка 4. Г. Нижний треугольник.
        # Кнопка 4. Г. Нижний треугольник.
        elif (value == 4):
            button4.lower_triangle()

        # value == 5. Кнопка 5. Д. Песочные часы.
        # Кнопка 5. Д. Песочные часы.
        elif (value == 5):
            button5.sand_clock()

        # value == 6. Кнопка 6. Е. Песочные часы на боку.
        # Кнопка 6. Е. Песочные часы на боку.
        elif (value == 6):
            button6.sand_clock_on_the_side()

        # value == 7. Кнопка 7. Ж. Левый треугольник.
        # Кнопка 7. Ж. Левый треугольник.
        elif (value == 7):
            button7.left_triangle()

        # value == 8. Кнопка 8. З. Правый треугольник.
        # Кнопка 8. З. Правый треугольник.
        elif (value == 8):
            button8.right_triangle()

        # value == 9. Кнопка 9. И. Левый верхний угол.
        # Кнопка 9. И. Левый верхний угол.
        elif (value == 9):
            button9.left_upper_angle()

        # value == 10. Кнопка 10. К. Правый нижний угол.
        # Кнопка 10. К. Правый нижний угол.
        elif (value == 10):
            button10.right_lower_angle()

        else:
            print('\nОшибка! Пожалуйста, выберите пункт от 1 до 10.\n')

    except ValueError:
        print('\nОшибка! Судя по всему, вы ввели буквы или спец. символы.')
        print('Пожалуйста, выберите пункт от 1 до 10.\n')
        continue

# break # выключен. Перезапускаем программу.