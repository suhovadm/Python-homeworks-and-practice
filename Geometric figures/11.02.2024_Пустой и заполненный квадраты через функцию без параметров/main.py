import empty_square
import filled_square

# Заводим главную функцию main, внутри которой будет крутиться 
# бесконечный цикл while.
def main():
    while(True):
        try:

            # Меню с выбором типа квадрата.
            print('[   Меню   ]')
            print('1. Пустой квадрат.')  # value 1.
            print('2. Заполненный квадрат.')  # value 2.
            print('3. Выход.') # value 3.

            # Приглашение к выбору типа квадрата.
            choice = int(input('Выберите тип квадрата (1, или 2):~$ '))

            # 1. Пустой квадрат.
            if (choice == 1):
                empty_square.kvadratS()

            # 2. Заполненный квадрат.
            elif (choice == 2):
                filled_square.kvadratS()

            # 3. Выход из программы.
            elif (choice == 3):
                print('\nДо новых встреч.')
                break

            else:
                print('\nОшибка! Пожалуйста, выберите пункт 1 или 2.\n')

        except ValueError:
            print('\nОшибка! Похоже, что вы ввели буквы или спец. символы.')
            print('Пожалуйста, выберите пункт 1 или 2.\n')
            continue

if __name__ == '__main__':
    main()
