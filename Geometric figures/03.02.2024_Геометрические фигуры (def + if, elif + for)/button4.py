# value == 4. Кнопка 4. Г. Нижний треугольник.
# Кнопка 4. Г. Нижний треугольник.

def lower_triangle():

    # С помощью value1 задаётся высота фигуры.
    value1 = int(input('Введите высоту нижнего треугольника:~$ '))

    # Правильный рэйнж для нижнего треугольника.
    for i in range(value1 -0):

        print(" " * (value1 - i), "*" * (2 * i + 1))