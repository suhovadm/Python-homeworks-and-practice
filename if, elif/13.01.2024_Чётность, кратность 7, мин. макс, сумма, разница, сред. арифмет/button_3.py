# ������ 3. �������� �� 2-� �����.
def handle_button_3():
        a = int(input('> ������� ������ ����� (��� ����� � �������):~$ '))
        b = int(input('> ������� ������ ����� (��� ����� � �������):~$ '))

        # ������ ��� ������� ������ 3. ������� 3.
        if a != b: # ���� � �� ����� b. ���������� �����.
            if a > b: # ���� � ������ b.
                print(f'\n   {a} ������ / ��������.\n')
            else:
                print(f'\n   {b} ������ / ��������.\n')
        else:
            print('\n����� �����.\n')