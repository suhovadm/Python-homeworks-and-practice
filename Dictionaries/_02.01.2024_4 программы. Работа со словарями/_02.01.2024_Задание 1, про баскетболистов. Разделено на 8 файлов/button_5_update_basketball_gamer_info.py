import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def update_info():
# Обновление информации в словаре.

    print('[ Вы находитесь в меню 5, обновление информации в словаре ]')
    print('[ Внимание! Ввод имени игрока чувствителен к регистру ]')
    name = input('Введите имя игрока (например, Michael Jordan):~$ ')
    if name in main_dict.basketball_gamers:
        name_of_band = input('Введите название команды:~$ ')
        number = input('Введите номер игрока:~$ ')
        height = input('Введите рост игрока:~$ ')
        print('Информация в словаре обновлена!') # Информация обновлена для меню 5.
        main_dict.basketball_gamers[name] = {'Команда: ' + name_of_band, 'Номер игрока: ' + number,  'Рост: ' + height + ' см.'}
        printer = pprint.PrettyPrinter(width=100, indent=1)
        printer.pprint(main_dict.basketball_gamers)
    else:
        print('Неправильно введено имя игрока!')
        print('Здесь нельзя добавлять новых игроков, можно только обновлять параметры у старых.')