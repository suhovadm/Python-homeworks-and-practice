# --- Задание 6: сформировать третий список, содержащий только минимальное
# и максимальное значение каждого из списков. ---

from main_random_lists import list1, list2

list7 = [min(list1), max(list1), min(list2), max(list2)]

# Статейка про min, max диапазона: https://pythonstart.ru/osnovy/min-max-python?ysclid=lscqvl155g849253268

print('5. Минимальное и максимальное:', list7)
print('-'*74)