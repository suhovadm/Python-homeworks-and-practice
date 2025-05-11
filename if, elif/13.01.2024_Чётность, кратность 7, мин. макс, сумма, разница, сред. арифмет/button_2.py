# Кнопка 2. Число кратное 7.
def handle_button_2():
        var2 = int(input('> Введите число кратное 7:~$ '))

        # Скрипт для обвязки кнопки 2. Задание 2.
        if var2 % 7 == 0:
            print(f'\n   {var2} кратно 7 / is mulptiple 7.\n')
        else:
            print(f'\n   {var2} не кратно 7 / is not multiple 7.\n')