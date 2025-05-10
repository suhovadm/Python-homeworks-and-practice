# ������: ������������ ������ ��������� 1 ������� ���������, ���������� � ������� ������.
# � ����������� �� ������ ������������ ��������� ����� ����� ������ ��� ��������� 1
# ��������� � ������ ������.
# ��� ���������� ����������� ������������ ��������� ��������� if / elif.
# �� �������: ������� ��������� �� ��������� ������ ��� ����� ��������� ����.

import main_menu
import button_1
import button_2
import button_3
import button_4

# ��������� ����������� ���� while.
while(True):
    try:

        # ����������� � ����� ������.
        value1 = float(input('> ������� ��������� ������� � ������ (����� ����� �����, ��� ��������):~$ '))
        value2 = int(input('> ������� ���������� �������� (������ ����� �����, ��� ����� � �������):~$ '))
        value3 = float(input('> ������� ������� ������ �� ������� (����� ����� �����, ��� ��������):~$ '))

        # ������� ������� � ������� ���� �� ����� main_menu.py
        main_menu.show_main_menu()

        # ����������� � ����� �������, ��� ��������� ����� ���������...
        choice = int(input('> ��� ����� ���������, ����� ����� ������, ��� ��������� 1 �������? '))

        if choice == 1:
            button_1.show_obshaya_summa_zakaza(value1, value2)

        elif choice == 2:
            button_2.show_obshaya_summa_zakaza_so_skidkoi(value1, value2, value3)

        elif choice == 3:
            button_3.show_stoimost_1_consoli_without_skidka(value1, value2)

        elif choice == 4:
            button_4.show_stoimost_1_consoli_so_skidkoi(value1, value2, value3)

        else:
            print('������! ������������ �����. ����������, ��������� �������.')

    except: continue

# break # �������. ������������� ���� while.