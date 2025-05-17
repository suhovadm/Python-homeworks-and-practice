import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def update_info():
    # Обновление информации в словаре.

    print('[ Вы находитесь в меню 5, обновление информации в базе данных ]')
    print('[ Внимание! Ввод имён и параметров сотрудников чувствителен к регистру ]')
    name = input('Введите имя сотрудника:~$ ')
    if name in main_dict.agents:
        phonenumber = input('Введите телефон сотрудника:~$ ')
        email = input('Введите e-mail:~$ ')
        jobtitle = input('Введите должность:~$ ')
        office = input('Введите имя, или номер офиса:~$ ')
        skype = input('Введите логин в Skype:~$ ')
        print('Информация в словаре обновлена!')  # Информация обновлена для меню 5.
        main_dict.agents[name] = {'Телефон: ' + phonenumber, 'e-mail: ' + email, 'Должность: ' + jobtitle, 'Офис: ' + office,
                        'Skype: ' + skype}
        printer = pprint.PrettyPrinter(width=100, indent=1)
        printer.pprint(main_dict.agents)
    else:
        print('Неверное имя сотрудника!')
        print('Нельзя обновить данные у несуществующей записи.')