# Способ №1: list(set(lst)), удаляет дубликаты, но нарушает порядок элементов.

# Способ №2: одной строкой, но та же логика. Через функцию.
# Подходит для быстрой фильтрации списков без потери порядка.
def remove_dups(seq):
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]

# Пример.
my_list = [1, 2, 2, 3, 3, 4, 4, 5, 1, 6, 7]

# Применяем функцию remove_dups для получения списка без дублей.
# Вгоняем my_list в функцию remove_dups, которая лежит внутри переменной unique_list.
unique_list = remove_dups(my_list)

# И распечатываем переменную unique_list.
print('Список без дублей:')
print(unique_list)