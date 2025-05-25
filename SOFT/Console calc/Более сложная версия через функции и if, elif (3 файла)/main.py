from main_menu import main_menu
from functions import *

while(True):

    # Подтягиваем функцию с главным меню из файла main_menu.py
    main_menu()

    choice = input('Пожалуйста, выберите пункт меню выше:~$ ')

    # Выход из программы по нажатию на ноль.
    if choice == '0':
        print('\nДо новых встреч.')
        break

    # Приглашение к вводу команд.
    # Ввод целых (дробных) значений с обработкой ошибок.
    try:
        a = float(input('Введите первое число:~$ '))
        b = float(input('Введите второе число:~$ '))
    except ValueError:
        print('\nОшибка! Введите числовое значение.\n')
        continue

    # Сложение.
    if choice == '1':
        result = add(a, b)
        print('\nРезультат:', result)

    # Вычетание.
    elif choice == '2':
        result = subtract(a, b)
        print('\nРезультат:', result)

    # Умножение.
    elif choice == '3':
        result = multiply(a, b)
        print('\nРезультат:', result)

    # Возведение в степень.
    elif choice == '4':
        result = power(a, b)
        print('\nРезультат:', result)

    # Деление.
    elif choice == '5':
        result = divide(a, b)
        print('\nРезультат:', result)

    else:
        print('\nОшибка! Неверный выбор операции.')

    # Пустая строка для разделения итераций.
    print()