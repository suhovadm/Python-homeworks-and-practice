import button_1_show_dict
import button_2_find_basketball_gamer_info
import button_3_add_basketball_gamer_info
import button_4_delete_basketball_gamer_info
import button_5_update_basketball_gamer_info

import main_menu

while(True): # Запускаем цикл. Цикл должен быть ПОД словарём, а не НАД ним,
    # иначе добавит только одну единственную запись и будет её перезаписывать.
    try:

        main_menu.menu()

        # Приглашение к вводу команды.
        menu = int(input('> Выберите пункт меню выше:~$ '))

        if (menu == 1):
            button_1_show_dict.show_dict()

        elif (menu == 2):
            button_2_find_basketball_gamer_info.show_info()

        elif (menu == 3):
            button_3_add_basketball_gamer_info.add_info()

        elif (menu == 4):
            button_4_delete_basketball_gamer_info.del_info()

        elif (menu == 5):
            button_5_update_basketball_gamer_info.update_info()

        # Выход из программы, остановка цикла While.
        elif (menu == 6):
            print('Чемпионат окончен. До новых встреч!')
            break

    except: continue