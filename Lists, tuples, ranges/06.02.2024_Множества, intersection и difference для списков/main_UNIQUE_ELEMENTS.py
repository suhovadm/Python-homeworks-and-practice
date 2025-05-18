# --- Задание 5: сформировать третий список, содержащий только уникальные элементы каждого из списков
# (то есть, отдельно для первого и отдельно для второго). ---

from main_random_lists import list1, list2

list6 = list(set(list1).difference(set(list2))) + list(set(list2).difference(set(list1)))

# set - множество, каждый элемент уникален,
# .difference - разность множеств для списков.
# Разностью множеств difference() называется множество,
# в которое входят все элементы первого множества, не входящие во второе множество.
# Статейка про .difference: https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-8-metody-raboty-so-mnozhestvami-2022-12-11?ysclid=lscq1si4lj837726934
# Раздел "Стандартные методы множеств Python".

print('4. Уникальные для каждого списка:', list6)