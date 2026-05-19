# Дан текстовый файл с числами. Опишите алгоритм, который находит максимальное число в файле.

filename = 'E:\mumbers.txt'

with open(filename, 'r', encoding='utf-8') as f:
    mumbers = list(map(int, f.read().split()))

if not mumbers:
    print('Файл пуст.')
else:
    max_number = max(mumbers)
    print('Максимальное число:', max_number)