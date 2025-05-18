# Задача: дано 3 кортежа с числами.
# Нужно найти уникальные числа в каждом из них.
# Для реализации функционала используйте генераторы списков.

# Заводим три кортежа. Специально делаем по одному уникальному числу в каждом.
# Все остальные числа должны быть одинаковыми.
numbers1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) # 0
numbers2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # 10
numbers3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11) # 11

# Запускаем генератор списков для первого кортежа. Проверяем, что данного элемента нет во 2-м и 3-м списках.
unique_elements = [element for element in numbers1 if element not in numbers2 and element not in numbers3]
print('Числа, уникальные для первого:', unique_elements)

# Запускаем генератор списков для второго кортежа. Проверяем, что данного элемента нет в 1-м и 3-м списках.
unique_elements = [element for element in numbers2 if element not in numbers1 and element not in numbers3]
print('Числа, уникальные для второго:', unique_elements)

# Запускаем генератор списков для третьего кортежа. Проверяем, что данного элемента нет в 1-м и 2-м списках.
unique_elements = [element for element in numbers3 if element not in numbers1 and element not in numbers2]
print('Числа, уникальные для третьего:', unique_elements)