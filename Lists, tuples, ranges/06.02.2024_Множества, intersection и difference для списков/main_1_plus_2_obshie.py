# --- Задание 4: сформировать третий список, содержащий элементы общие для двух списков. ---

from main_random_lists import list1, list2

list5 = list(set(list1).intersection(list(set(list2))))

# list - формирует список,
# set - множество, где каждый элемент уникален,
# .intersection - возвращает новый набор элементов, общий для двух списков.
# .intersection смотрит, какие множества пересекаются и выводит их в один общий список - list5.
# Статейка про .intersection: https://pythonstart.ru/set/intersection-python?ysclid=lscpkb9i2r864092533

print('3. Общие для каждого списка:', list5)