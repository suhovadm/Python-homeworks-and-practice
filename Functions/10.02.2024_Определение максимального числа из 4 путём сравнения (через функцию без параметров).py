# ������: �������� ����������� (�� �����������) ������� ��� ����, ����� ������,
# ����� �� ������ �������� ������������� ����� ������ ������.

# ��������� ����������� ����, ����� ��������� �� �����������.
while(True):
    try:

        # ���������� ������� ��� ������ ������������� ����� �� ������.
        def maxnumber():

            # ������ ����������� � ����� ������ ��� ������ ����� �����.
            value1 = int(input('������� ������ �����:~$ '))
            value2 = int(input('������� ������ �����:~$ '))
            value3 = int(input('������� ������ �����:~$ '))
            value4 = int(input('������� �������� �����:~$ '))

            # ���������, ��� value1 ������ ��� ������.
            if value1 > value2 and value1 > value3 and value1 > value4:
                print('������������ �����:', value1)  # �������� value1.

            # ���������, ��� value2 ������ ��� ������.
            elif value2 > value1 and value2 > value3 and value2 > value4:
                print('������������ �����:', value2)  # �������� value2.

            # ���������, ��� value3 ������ ��� ������.
            elif value3 > value1 and value3 > value2 and value3 > value4:
                print('������������ �����:', value3)  # �������� value3.

            # ���������, ��� value4 ������ ��� ������.
            elif value4 > value1 and value4 > value2 and value4 > value3:
                print('������������ �����:', value4)  # �������� value4.

        maxnumber()  # ��������� ������� ��� ������ ������������� ����� �� ������.

    except: continue