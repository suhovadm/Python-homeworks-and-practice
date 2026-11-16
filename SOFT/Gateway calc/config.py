# Настройки кодировки и лимиты истории команд.

import sys # Работа с вводом, выводом и завершением программы.

# Принудительно включаем кодировку UTF-8 для корректного ввода русских символов.
if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8")

# Вывод. Чтобы русский текст корректно отображался в консоли.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Максимальное количество команд в истории.
HISTORY_LIMIT = 100

# Допустимые границы длины префикса IPv4.
MIN_PREFIX = 1
MAX_PREFIX = 30