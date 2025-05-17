import button_1_open_dict
import button_2_find_info_in_dict
import button_3_add_info_in_dict
import button_4_delete_info_from_dict
import button_5_update_info_in_dict

import main_menu

while(True): # Запускаем цикл. Цикл должен быть ПОД словарём, а не НАД ним.
    # Иначе будет добавлять лишь одно значение и обновлять его!
    try:

        main_menu.menu()

        # Выбор пункта основного меню программы.
        menu = int(input('>  Выберите пункт меню выше:~$ '))

        # Открыть библиотеку (посмотреть словарь).
        if (menu == 1):
            button_1_open_dict.show_dict()

        # Найти информацию в библиотеке.
        elif (menu == 2):
            button_2_find_info_in_dict.find_info()

        # Добавить новое произведение, или обновить информацию о существующем.
        elif (menu == 3):
            button_3_add_info_in_dict.add_info()

        #  Удалить информацию о произведении.
        elif (menu == 4):
            button_4_delete_info_from_dict.del_info()

        # Обновление информации в библиотеке (в словаре).
        elif (menu == 5):
            button_5_update_info_in_dict.update_info()

        # Выход из программы, остановка цикла While.
        elif (menu == 6):
            print('Не забудьте читательский билет.')
            break

    except: continue