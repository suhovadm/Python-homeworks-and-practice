import main_dict
import pprint # Подключаем библиотеку для красивого вывода словарей и списков.

def update_info():
# Обновление информации в словаре.

    print('[ Вы находитесь в меню 5, обновление информации в словаре ]')
    print('[ Внимание! Ввод слов чувствителен к регистру ]')
    name = input('Введите слово на английском (например, cat, dog, bear и т.д.):~$ ')
    if name in main_dict.words:
        parameter = input('И перевод на французский:~$ ')
        print('Информация в словаре обновлена!') # Информация обновлена для меню 5.
        main_dict.words[name] = parameter
        printer = pprint.PrettyPrinter(width=100, indent=1)
        printer.pprint(main_dict.words)
    else:
        print('Такого слова в словаре нет!')
        print('Здесь нельзя добавлять новые слова, можно только обновлять старые.')