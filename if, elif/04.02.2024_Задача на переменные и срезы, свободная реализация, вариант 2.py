# ������ �� ���������� � �����.
# ������������ ������ �����, ��� ��������������,
# c ���� ����� �������� ��� ��������:

# 1) ��� �������� � �������� �������,
# 2) ������� ������ ����� ������,
# 3) ������ �������� �� �������,
# 4) �������� �������� �� �������,
# 5) ��� �������� ������� � ������� ������������,
# 6) ��� �������� �� ������ �� �������,
# 7) ��� �������� �� �������������� �� �������� � �������� �������.

# ���������� ����������� ����� ������� � ��������� �����:
# ����� ����������, �����, ��������� �����, ��������� ��������� � ����������� ����.

# ������� 2.

def menu_item_1(value):
    return value[::-1] # ��� �������� � �������� �������

def menu_item_2(value):
    return value[:] # ������� ������ ����� ������

def menu_item_3(value):
    return value[1::2] # ������ �������� �� �������

def menu_item_4(value):
    return value[::2] # �������� �������� �� �������

def menu_item_5(value):
    return value[5:] # ��� �������� ������� � ������� ������������

def menu_item_6(value):
    return value[:5] # ��� �������� �� ������ �� �������

def menu_item_7(value):
    return value[-2:1:-1] # ��� �������� �� �������������� �� �������� � �������� �������

# ������� � �������. ������ �������� - ��� ������� ����.
menu_functions = {
    1: menu_item_1,
    2: menu_item_2,
    3: menu_item_3,
    4: menu_item_4,
    5: menu_item_5,
    6: menu_item_6,
    7: menu_item_7
}

menu_text = """
��� ����� �������?
1. �� � �������� �������?
2. ������ ����� ������.
3. ׸���� �� �������.
4. �������� �� �������.
5. ��� �������� ������� � �������.
6. ��� �������� �� �������.
7. �� �������������� �� �������� � �������� �������.
8. �����.
"""

while(True):
    print(menu_text)
    try:

        choice = int(input('�������� ����� ���� ����:~$ '))

        if choice == 8:
            print('\n�� ����� ������!')
            break

        elif choice not in range(1, 8):
            print('\n����������, �������� ����� �� 1 �� 8.')
            continue

        value = input('������� �����, ��� ��������������:~$ ')

        result = menu_functions[choice](value)
        print('\n���������:\n', result)

    except ValueError:
        print('\n������! ����������, ������� ����� �� 1 �� 8.')