from dictionary import students

# 1. Добавить студента.
def add_student(name, grade):
    if name in students:
        print(f'\nСтудент {name} уже есть в списке.')
    else:
        students[name] = grade
        print(f'\nСтудент {name} добавлен с оценкой {grade}.')

# 2. Посмотреть студентов и их оценки.
def show_students():
    print('Список студентов и их оценки.')
    print()
    for name, grade in students.items():
        print(f'{name}: {grade}')

# 3. Посмотреть средний балл.
def show_average_score():
    if students:
        # sum(students.value()) - сумма всех оценок.
        # len(students) - количество студентов.
        # Делим сумму всех оценок на количество студентов, получаем средний балл.
        average_score = sum(students.values()) / len(students)
        # Что означает .2f ?
        # .2 - означает оставить только два знака после запятой.
        # f - означает форматировать число с плавающей точкой, то есть float.
        print(f'\nСредний балл всех студентов: {average_score:.2f}')
    else:
        print('\nСписок студентов пуст.')

# 4. Удалить студента.
def delete_student(name):
    if name in students:
        del students[name]
        print(f'\nСтудент {name} удален из списка.')
    else:
        print(f'\nСтудент {name} не найден.')