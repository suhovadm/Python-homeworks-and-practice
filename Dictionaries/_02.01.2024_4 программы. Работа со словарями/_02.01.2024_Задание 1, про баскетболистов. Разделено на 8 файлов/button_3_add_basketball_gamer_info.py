import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def add_info():
# Добавить информацию о баскетболисте.

            print('[ Вы находитесь в меню 3, добавление информации ]')
            print('[ Если ввести уже существующее имя игрока, информация о нём будет обновлена ]')
            name = input('Введите имя игрока (например, Dennis Rodman):~$ ')
            name_of_band = input('Введите название команды:~$ ')
            number = input('Введите номер игрока:~$ ')
            height = input('Введите рост игрока:~$ ')
            main_dict.basketball_gamers[name] = {'Команда: ' + name_of_band, 'Номер игрока: ' + number, 'Рост: ' + height + ' см.'}
            print('Информация в словаре обновлена!') # Информация обновлена для меню 3.
            printer = pprint.PrettyPrinter(width=100, indent=1)
            printer.pprint(main_dict.basketball_gamers)