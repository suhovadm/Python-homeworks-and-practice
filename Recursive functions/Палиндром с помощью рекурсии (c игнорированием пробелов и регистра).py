# ��������� ����������� ������� ��� �������� ����������.
# ��������� ������� ������������� �������� � �������� ��� ����� ������ �������������.

def palindrom(stroka): # ������� ������� � ���������� stroka.

    # ������ ����� ������� �� �����.
    if len(stroka) <= 1: # ���� ����� ������ ������, ��� ����� 1, ������ ��� ���������, �� ����
        return True # True. �������� ���������, �������.

    # ���� �� ����� ���� �� �������, � ������� ����� 1 �������.
    else:
        # ���������� ����� ������ ����� � ��� �� ������ �� ��������.
        if stroka[0] == stroka[-1]: # ���� ������� ������ ����� ����������, �����
            return palindrom(stroka[1:-1]) # ���������� ������ �� ������� �� ���������� �������.
        else: # ���� �� �����, �����
            return False # False, �.�. �� ���������.

value = input('������� ������:~$ ') # ����������� � ����� �������. ����� ������� str, ��������� ������ input.

# ������� ������� � �������� ������ � ������� ��������.
normalized_value = value.replace(' ', '').lower()

# ������� �������� normalized_value (������) � ������� palindrom.
if palindrom(normalized_value): # ���� ������ ������� �� 1 �������, ��� ������� �� ������� �� ���������� �����,
    print('���������!') # ������ ��� True - ���������. ��� ������ ������ ���� �������� - ��� ���� ���������.
else: # ���� ���, �����
    print('�� ���������.') # �� ���������.