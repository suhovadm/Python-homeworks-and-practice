﻿# Написание рекурсивной функции для поиска индекса элемента в отсортированном массиве.

# Заводим функцию find_index_recursive с 3-я параметрами.

# list1 - первый параметр функции, который представляет собой список, в котором мы будем искать элемент.
# target - второй параметр функции, который представляет собой сам элемент, индекс которого нам нужно найти в списке.
# index=0 - третий параметр функции со значением по умолчанию. Это текущий индекс, который мы будем проверять в
# списке. По умолчанию он равен 0, что означает, что поиск начнётся с первого элемента.

def find_index_recursive(list1, target, index=0):

    # Базовый случай для рекурсии.
    # Здесь мы проверяем, не вышли ли мы за пределы списка. Если текущий index больше или равен длине
    # списка len(list1), значит, мы проверили все элементы и целевой элемент не найден. В этом случае
    # функция возвращает нам -1, что указывает на то, что элемент не существует в списке.

    if index >= len(list1):
        return -1  # Если элемент не найден, возвращаем -1.

    # Проверка текущего элемента.
    # Здесь мы сравниваем текущий элемент списка list1 по индексу (index) с целевым элементом target.
    # Если они равны, значит, что мы нашли нужный элемент, и возвращаем текущий индекс.

    if list1[index] == target:
        return index

    # Рекурсивный вызов функции.
    # Если текущий элемент не равен целевому, мы вызываем функцию find_index_recursive снова, увеличивая
    # индекс на 1 (index + 1). Это значит, что мы переходим к следующему элементу списка и продолжаем поиск.

    return find_index_recursive(list1, target, index + 1)

# Заводим рандомный список, заводим цель (target), она будет под индексом 0.
list1 = [7, 2, 5, 6]
target = 7

# Принтуем список на экран. Если надо вывести отсортированный список, то это делается так:
# print(sorted(list1)), тогда все цифры в списке будут выведены от меньшего к большему.
print((list1))

# Принтуем надпись, которая покажет нам, под каким индексом цель находится в списке.
# В данном случае, семёрка находится под нулевым индексом в списке.
print('Элемент находится в списке под индексом:', find_index_recursive(list1, target))