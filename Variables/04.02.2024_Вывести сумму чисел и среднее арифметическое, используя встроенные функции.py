# ������ �� ����������. ������������ ������ � ������ ��� ����� �����.
# ����� ��������� ����� ���� ����� � ������� ��������������
# ��� ���������� ����������� ���������� �������.

# ��������� ����������� ���� while.
while(True):
    try:

        # ����������� � ����� �������.
        # .split() - ��������� �������� ������ �� �������� � ���������� ������ �����.
        # map(int, ...) - ��������� ������� int � ������� �������� ������, ���������� ������ � ����� �����.
        # list(...) - ���������� ��������� map � ������ ����� �����, ������� ����������� � ���������� value1.
        value1 = list(map(int, input('������� ����� ����� ������:~$ ').split()))

        # sum(value1) - ��������� ����� ���� ����� � ������.
        # len(value1) - ���������� ���������� �����, �������� �������������.
        # sum(value1) / len(value1) - ������������ ������� ��������������.
        print('\n����� �����:', sum(value1),'; ������� ��������������:', sum(value1) / len(value1),'\n')

    except: continue

# break # ��������.

