# ������ �� ����������.
# ����� ���������� ���������� ����, ������������� � ������.
# ����������� ������ ���������� � ���������� ������.
# �������� ��������� ������, ����� ������������ �� ��� ������� ����� � �������.

# ��������� ����������� ���� while.
while(True):
    try:

        # ����������� � ����� �������.
        value1 = list(map(int, input('������� ����� ����� ������:~$ ').split()))
        # .split() - ��������� �������� ������ �� ��������, �������� ������ �����.
        # map(int, ...) - ��������� ������� int � ������� �������� ������ �����, ���������� �� � ����� �����.
        # list(...) - ���������� ��������� map � ������ ����� �����.
        # � �����, ���������� value1 �������� ������ ����� �����, �������� �������������.

        number = int(input('������� ����� ��� ������ ������ ������ ����:~$ '))
        # number - ����������, ������ ������ ��������, �������� �������������. ��� ������ ������ ������.
        # int(input() - ���� �������������� ��������, �� ���� �����.

        print('\n���� ����� �����������',value1.count(number), '���(�).\n')
        # ������� �� ����� ���������� ���, ������� ����� number ����������� � ������ value1.
        # .count(number) - ��� ���������� ����� ������, ������������ ����� ��������� �������� number.

    except ValueError:
        print('\n������! ����� ������� ������ �������� ��������.\n')
        continue

# break # ��������. ������������� ���������.