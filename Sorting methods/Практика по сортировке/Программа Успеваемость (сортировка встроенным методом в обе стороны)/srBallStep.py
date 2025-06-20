# 2.
# Определяем функцию srBallStep, которая принимает в себя 2 аргумента - srBall и spisok.
# srBall - это переменная для определения среднего балла, spisok - это список оценок.
def srBallStep(srBall, spisok):

    # Внутри функции вычисляем средний балл. Заводим переменную n, как сумму всех оценок
    # в списке, делённую на количество оценок. Количество оценок нам даёт len.
    n = sum(spisok) / len(spisok)

    # Затем проверяем, что n меньше 10.
    # Если да, то выводится стипендия.
    if n < 10:
        print('\nСтипендии нет.\n')
    else:
        print('\nСтипендия есть.\n')