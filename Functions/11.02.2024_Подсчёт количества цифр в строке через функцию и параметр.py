# ������: ������������ ������ ��������� �����. ����� �������� ������� ��� ��������
# ����� � ������. ����� ������������ ���� for, � ����� ���������� ����� len, ���
# ���������� ����� ������ � �������� �������������� ��������, �.�. ����� ����� ������.

while(True):

    # ������� ������� � ������ cifr_in_number � ���������� x � �������� ���������.
    def cifr_in_number(x):

        # ������� ������� ��� �������� ���� ������ ������.
        result = 0

        # ��������� ���� for ��� ��������� x.
        # ������� ���������� ���������� x ��� ������ � ������� str.
        # �����, ���������� ����� ������ � ������� len.
        for i in range(len(str(x))):

            # �������� ������� � ������� ��� ������� ������ ������.
            result += 1

            # ���������� ���������� � �����������.
        return result

            # ����������� � ����� ������� (�����).
    user_input = input('����������, ������� �����:~$ ')

    print('-' * 31)

    # ����� ������� � �������� ������������� ������ (���������).
    print('���������� ���� � �����', user_input, '=', cifr_in_number(user_input),'\n')


