# value == 3. Кнопка 3. В. Верхний треугольник.
# Кнопка 3. В. Верхний треугольник.

def upper_triangle():

    # С помощью value1 задаётся высота фигуры.
    value1 = int(input('Введите высоту верхнего треугольника:~$ '))

    # Правильный рэйнж для верхнего треугольника.
    for i in range(value1 -1, -1, -1):

        print(" " * (value1 - i), "*" * (2 * i + 1))