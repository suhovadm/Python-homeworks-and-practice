# Здесь живёт проверка IPv4, маска подсети и расчёт параметров сети.

from config import MIN_PREFIX, MAX_PREFIX

import ipaddress                         # Проверка IP-адресов, масок и расчёт подсетей.

# Проверяем IPv4 и маску, возвращаем объект сети.
# Здесь мы преобразуем введённый IP-адрес в объект IPv4Address.
# Если адрес некорректен, вызывается исключение ValueError.
def parse_subnet(ip_text: str, mask_text: str):
    ip = ipaddress.IPv4Address(ip_text)

    # Если строка состоит только из цифр, считаем её длиной префикса CIDR.
    # Например, значение 28 означает маску /28.
    if mask_text.isdigit():
        prefix = int(mask_text)

        # Разрешаем префиксы от /1 до /30 включительно.
        # /0, /31, /32 не поддерживаются.
        if not MIN_PREFIX <= prefix <= MAX_PREFIX:
            raise ValueError("Недопустимая длина префикса.")

        # Создаём объект сети. strict=False разрешает передать IP узла, а не только адрес самой сети.
        # Например, 192.168.1.100/24 преобразуется в сеть 192.168.1.0/24.
        network = ipaddress.IPv4Network(
            f"{ip}/{prefix}", strict=False
        )

    # Если введены не только цифры, считаем строку маской в формате
    # IPv4, например 255.255.255.240.
    else:
        mask = ipaddress.IPv4Address(mask_text)

        # Создаём сеть на основании IP и маски подсети.
        # Проверяем, что маска корректна:
        # единицы в двоичной записи должны идти перед нулями.
        network = ipaddress.IPv4Network(
            f"{ip}/{mask}", strict=False
        )

        # Получаем длину префикса из объекта сети.
        # Например, маска 255.255.255.240 — это /28.
        prefix = network.prefixlen

        # Проверяем, что длина префикса находится в допустимом диапазоне.
        if not MIN_PREFIX <= prefix <= MAX_PREFIX:
            raise ValueError("Недопустимая маска подсети.")

    # Возвращаем IP-адрес и уже рассчитанную сеть с её маской и границами.
    return ip, network

# Рассчитываем параметры IPv4-подсети.
# Принимаем IP и маску, проверяем данные и выводим результат.
def calculate_subnet(ip_text: str, mask_text: str) -> None:
    # Все потенциально некорректные данные обрабатываем здесь.
    try:
        # Проверяем IP и маску, получаем объект сети.
        ip, network = parse_subnet(ip_text, mask_text)

        # network.network_address — это адрес сети.
        # Прибавляем 1, чтобы получить первый обычный адрес узла.
        first_ip = network.network_address + 1

        # network.broadcast_address — широковещательный адрес.
        # Вычитаем 1, чтобы получить последний обычный адрес узла.
        last_ip = network.broadcast_address - 1

        # Выводим результаты.
        # Конструкция {'IP:':35} выделяет 35 символов под название поля,
        # благодаря чему значения располагаются в одном столбце.
        print()
        print(f"{'IP:':35}{ip}")
        print(f"{'Маска:':35}{network.netmask}")
        print(f"{'Префикс:':35}/{network.prefixlen}")
        print(f"{'Сеть:':35}{network.network_address}")
        print(f"{'Broadcast:':35}{network.broadcast_address}")
        print(f"{'Первый доступный адрес:':35}{first_ip}")
        print(f"{'Последний доступный адрес:':35}{last_ip}")

        # num_addresses — общее число адресов в подсети.
        # Для обычных подсетей IPv4 вычитаем 2:
        # один адрес сети и один broadcast-адрес.
        print(
            f"{'Количество доступных адресов:':35}"
            f"{network.num_addresses - 2}"
        )
        print()

    # Если IP или маска некорректны, сообщаем об ошибке,
    # но не завершаем программу — пользователь сможет повторить ввод.
    except ValueError:
        print()
        print("Некорректный IP-адрес или маска.")
        print()