# 2.
# Функция сортировки пузырьком по убыванию.
# Заводим функцию bubble_sort2, которая принимает в себя 1 аргумент - spisok, это тот же список оценок.
def bubble_sort2(spisok):
    # swapped = True, swapped = False нужны для того, чтобы запустить цикл While один раз.
    # Цикл while должен называться swapped.
    # swapped = True - инициируем переменную swapped, чтобы войти в цикл.
    # Имена переменных и самого цикла должны совпадать. Если написать While True, работать не будет.
    swapped = True
    while swapped:
        swapped = False

        # Запускаем цикл for, перебираем индексы элементов списка, кроме последнего, чтобы сравнивать соседние.
        # len - Даст нам количество элементов в объекте.
        for i in range(len(spisok) - 1):

            # Если текущий элемент МЕНЬШЕ следующего, меняем их местами.
            if spisok[i] < spisok[i + 1]:
                # Меняем элементы местами.
                spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]

                # Если обмен произошёл, отметим, что есть изменения, чтобы пройти цикл ещё раз.
                # То есть, устанавливаем swapped в True для следующей итерации.
                # Это классическая реализация пузырьковой сортировки по убыванию.
                swapped = True