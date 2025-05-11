import main_menu # Функция с главным меню программы.
import button_1 # Fizz / числа кратные 3-м.
import button_2 # Buzz / числа кратные 5-и.
import button_3 # Fizz Buzz / числа кратные и 3-м и 5-и.
import button_4 # Числа НЕ кратные 3-м и 5-и.

# Запускаем бесконечный цикл while.
while (True):
    try:

        # Приглашение к вводу команд.
        value1 = int(input('Введите первое число:~$ '))  # value1, значение 1.
        value2 = int(input('Введите второе число:~$ '))  # value2, значение 2.

        # Подтягиваем главное меню из файла main_menu.py
        main_menu.show_main_menu()

        # Выбираем пункт меню из файла main_menu.py выше.
        value = int(input('Выберите пункт меню выше (введите число от 1 до 5):~$ '))

        # Проверка, чтобы пользователь ввёл именно цифры от 1 до 5.
        if value < 1 or value > 5:
            print('\nПожалуйста, введите число от 1 до 5.\n')
            continue

        # Fizz / числа кратные 3-м.
        if value == 1:
            button_1.handle_fizz(value1, value2)

        # Buzz / числа кратные 5-и.
        elif value == 2:
            button_2.handle_buzz(value1, value2)

        # Fizz Buzz / числа кратные и 3-м и 5-и.
        elif value == 3:
            button_3.handle_fizz_buzz(value1, value2)

        # Числа НЕ кратные 3-м и 5-и.
        elif value == 4:
            button_4.handle_non_multiplies(value1, value2)

        # Выход из программы.
        elif value == 5:
            print('\nДо новых встреч.')
            break

    # Обработчик ошибок, чтобы пользователь не мог вводить буквы вместо цифр.
    except ValueError:
        print('\nОшибка! Пожалуйста, введите корректное числовое значение.\n')
        continue

    # Общий обработчик ошибок, чтобы программа не прерывалась.
    except:
        continue

# break # выключен.