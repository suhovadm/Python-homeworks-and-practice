import button_1_show_dict
import button_2_find_info_in_dict
import button_3_add_info_in_dict
import button_4_delete_info_in_dict
import button_5_update_info_in_dict

import main_menu

while(True): # Запускаем цикл. Словарь должен быть над while(True), а не внутри него, иначе
    # будет добавлять один единственный параметр и обновлять его.
    try:

        main_menu.menu()

        # Приглашение к вводу команды.
        menu = int(input('>  Выберите пункт меню выше:~$ '))

        # Посмотреть словарь.
        if (menu == 1):
            button_1_show_dict.show_dict()

        # Найти информацию в словаре.
        elif (menu == 2):
            button_2_find_info_in_dict.find_info()

        # Добавить информацию в словарь.
        elif (menu == 3):
            button_3_add_info_in_dict.add_info()

        # Удалить информацию из словаря.
        elif (menu == 4):
            button_4_delete_info_in_dict.del_info()

        # Обновление информации в словаре.
        elif (menu == 5):
            button_5_update_info_in_dict.update_info()

        # Выход из программы, остановка цикла While.
        if (menu == 6):
             print('До свидания.')
             break

    except: continue