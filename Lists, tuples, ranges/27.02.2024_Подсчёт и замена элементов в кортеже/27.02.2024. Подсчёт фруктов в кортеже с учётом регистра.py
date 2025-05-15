# Задача: посчитать количество фруктов в кортеже.

while(True):
    try:

        tuple = (('Apple', 'Apple', 'Strawberry', 'Banana', 'banana', 'banana', 'mango'))
        print(tuple)
        value1 = input('Введите название фрукта (с учётом регистра):~$ ')
        print('\nКоличество слов в кортеже:',tuple.count(value1),'\n')

    except: continue