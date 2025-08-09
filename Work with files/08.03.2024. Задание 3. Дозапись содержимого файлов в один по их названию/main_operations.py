# ------ Обвязка условий сравнения и вывод в файл FINAL.txt на дозапись. ------

def process_file_choice(value1, content1, content2, content3):

    # Для первого файла - условие сравнения in.txt (в нижнем регистре для вывода):
    if value1 == ('in.txt'): # Если value1 == in.txt

        # Открываем FINAL.txt на дозапись
        with open('FINAL.txt', 'a', encoding='utf-8') as f4:

            # и записываем в него content1.
            f4.write(f'\n{content1}')

    # Для второго файла - условие сравнения middle.txt (в нижнем регистре для вывода):
    if value1 == ('middle.txt'): # Если value1 == middle.txt

        # Открываем FINAL.txt на дозапись
        with open('FINAL.txt', 'a', encoding='utf-8') as f4:

           # и записываем в него content2.
           f4.write(f'\n{content2}')

    # И для третьего - условие сравнения out.txt (в нижнем регистре для вывода):
    if value1 == ('out.txt'): # Если value1 == out.txt

        # Открываем FINAL.txt на дозапись
        with open('FINAL.txt', 'a', encoding='utf-8') as f4:

            # и записываем в него content3.
            f4.write(f'\n{content3}')