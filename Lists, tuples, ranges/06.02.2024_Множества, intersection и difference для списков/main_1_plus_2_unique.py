# --- Задание 3: сформировать третий список, содержащий элементы обоих списков БЕЗ повторений. ---

# В данном случае, подтягиваем не list1 + list2, а сразу list3
# из третьего файла - main_1_plus_2.py
from main_1_plus_2 import list3

# list - формирует список, set - показывает множество, в котором каждый элемент уникален.
# ? Возможно, здесь list указан лишний раз, так как список у нас уже есть, но всё работает. ?
list4 = list(set(list3))

# Про множества: https://python-scripts.com/sets?ysclid=lscqxkw1np748565318
# Про множества: https://habr.com/ru/companies/wunderfund/articles/693592/
# Про множества: https://pythonru.com/osnovy/mnozhestva-v-python?ysclid=lscserboay513930815

# Принтуем четвёртый список в котором каждый элемент уникален.
print('2. Без повторений:', list4)