# Задача: посчитать количество слов, в том числе тех, которые являются частью других слов.

# Рабочий вариант, не потерять:
# https://translated.turbopages.org/proxy_u/en-ru.ru.255cd768-65dd9a17-5bd61493-74722d776562/https/stackoverflow.com/questions/74903185/how-to-find-every-instance-of-a-word-in-a-tuple-python

while(True):
    try:

        tuple = (('Apple', 'Apple', 'apple', 'Strawberry', 'banana', 'bananamango', 'Mango', 'Strawberry-banana', 'appleapple'))
        print(tuple)
        value1 = input('Введите слово для поиска (с учётом регистра):~$ ')
        count = ' '.join(tuple).count(value1)
        print('\nКоличество слов в кортеже:',count,'\n')

    except: continue
