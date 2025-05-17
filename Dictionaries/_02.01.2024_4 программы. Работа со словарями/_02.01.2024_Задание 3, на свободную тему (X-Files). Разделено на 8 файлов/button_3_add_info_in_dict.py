import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def add_info():
    # Добавить информацию в словарь.

    print('[ Вы находитесь в меню 3, добавление информации в базу данных ]')
    print('[ Если ввести уже существующее имя сотрудника, информация о нём будет обновлена ]')
    name = input('Введите имя сотрудника:~$ ')
    phonenumber = input('Введите телефон сотрудника:~$ ')
    email = input('Введите e-mail:~$ ')
    jobtitle = input('Введите должность:~$ ')
    office = input('Введите имя, или номер офиса:~$ ')
    skype = input('Введите логин в Skype:~$ ')
    main_dict.agents[name] = {'Телефон: ' + phonenumber, 'e-mail: ' + email, 'Должность: ' + jobtitle, 'Офис: ' + office,
                    'Skype: ' + skype}
    print('Информация в базе данных обновлена!')  # Информация обновлена для меню 3.
    printer = pprint.PrettyPrinter(width=120, indent=1)
    printer.pprint(main_dict.agents)  # В данном случае, выводит всю базу данных (словарь).