# ������: �������� ���������, ������� � ������� ���������� ��������� if / elif
# �������� ����������� �������������� �������� � ����� �������. ��������, ���������,
# ���������, �������. � ��������� ������ ���� ���� � ����������� ������.
# �������� ��������� ������ � 4 ������, ����� ������ ���� ������ �� ����.

# ��������� ����.
while(True):
    try:

            # ����.
            print('1. ��������.') # value 1.
            print('2. ���������.') # value 2.
            print('3. ���������.') # value 3.
            print('4. �������.') # value 4.
            print('5. �����.') # value 5.

            # ����� ������ ���� ����.
            value = int(input('�������� �������������� �������� (�� 1 �� 4):~$ '))

            # ������ 1. ����� ���� �����.
            if (value == 1):

                # ����������� � ����� �������, � ����� ������, ����� ����� ������.
                # value1 = input - ��� ���� ������������� ������� �����.
                value1 = input('����� ���� ����� ������ (��������, 23+12):~$ ')

                # numbers - ������ ��� ������Ĩ���� � �����, �� ���� � ������, ����� � ����������� ������.
                # .split() - ��������� ��������, �������� �������������, � ������.
                # ���� " + " � ������ ������, ����� ��������� ������������ ����� ���������� ������. �� �� ���������.
                numbers = value1.split('+')

                # ������ ����� ������� ����� �� ����. �� ����, �� ��� �� ����� ����������, ��������, �������� � ������.
                # ��� �������� � ������� ���� ���������� - a � b.
                a = int(numbers[0]) # ���������� � - ������ ����� ������, ��� ���������� ��� 0.
                b = int(numbers[1]) # ���������� b - ������ ����� ������, ��� ���������� ��� 1.

                # ���������� result, � ������� �� .split-a ��� ������� ���������� ���������� a � b,
                # .split ��, ������ ������� ��� ������ �������.
                result = a + b

                # �������� ���������.
                # value1 - ��� ��, ��� ������ ������������.
                # result - ��� ��������������� ��� ���������, �� ����, ��, ��� ����������.
                print('\n',f'����� ����� {value1} ����� {result}','\n')

                # ������ 2. ������� ���� �����.
            elif (value == 2):
                value1 = input('������� ���� ����� ������ (��������, 23-12):~$ ')
                numbers = value1.split('-')
                a = int(numbers[0])
                b = int(numbers[1])
                result = a - b
                print('\n',f'������� ����� {value1} ����� {result}','\n')

                # ������ 3. ������������ ���� �����.
            elif (value == 3):
                value1 = input('������������ ���� ����� ������ (��������, 23*12):~$ ')
                numbers = value1.split('*')
                a = int(numbers[0])
                b = int(numbers[1])
                result = a * b
                print('\n',f'������������ ����� {value1} ����� {result}','\n')

                # ������ 4. ������� ���� �����.
            elif (value == 4):
                try:

                    value1 = input('������� ���� ����� ������ (��������, 23/12):~$ ')
                    numbers = value1.split('/')
                    a = int(numbers[0])
                    b = int(numbers[1])
                    result = a / b
                    print('\n', f'������� ���� ����� {value1} ����� {result}', '\n')

                except ZeroDivisionError:
                    print('\n������! �� ���� ������ ������.\n')
                except (ValueError, IndexError):
                    print('\n������������ ������ �����. ���������� ��� ���.\n')

                # ������ 5. ����� �� ���������.
            elif (value == 5):
                print('\n����� �� ���������.')
                break

            else:
                print('\n������������ �����. ����������, �������� ����� �� 1 �� 5.\n')

    except: continue

# break # ��������, ������������� ���������...