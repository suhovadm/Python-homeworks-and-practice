# Кнопка 3. Fizz Buzz / числа кратные и 3-м и 5-и.
def handle_fizz_buzz(value1, value2):

    # Показывает диапазон между числами.
    for i in range(value1, value2 + 1):

        # Выводит числа кратные и 3-м и 5-и.
        if (i % 3 == 0) or (i % 5 == 0):

            # Если числа кратны и 3-м и 5-и, подгоняет к ним надпись ' Fizz Buzz '.
            print(i, '/ Fizz Buzz.')