# Здесь живут очистка экрана, ввод данных и обработка команд - history, cls, clear, exit и quit.

from history import add_history_entry, show_history

import os               # Выполнение системных команд, например, очистка экрана.
import sys              # Работа с вводом, выводом и завершением программы.

# Очистка экрана.
def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

# Приглашение к вводу команд. Тип ввода: str.
# Приглашение к вводу команд крутится в бесконечном цикле, ничего перезапускать не надо.
def read_input_command(prompt: str) -> str:
    while(True):
        try:
            value = input(f"{prompt}: ")

        # EOFError возникает при завершении ввода,
        # KeyboardInterrupt при нажатии Ctrl + C.
        except (EOFError, KeyboardInterrupt):
            print("\nЗавершение программы.")
            sys.exit(0)  # Завершаем программу без ошибки.

        # Сохраняем введённую строку в истории.
        add_history_entry(value)

        # Убираем пробелы по краям и переводим текст в нижний регистр.
        # Благодаря этому HISTORY и history воспринимаются одинаково.
        command = value.strip().lower()

        # Если введены команды exit или quit - завершаем программу.
        if command in ("exit", "quit"):
            print("\nЗавершение программы.")
            sys.exit(0)

        # При вводе cls или clear очищаем консоль и повторяем запрос ввода.
        if command in ("cls", "clear"):
            clear_screen()
            continue

        # Если введена history — показываем историю команд.
        if command == "history":
            show_history()

            # Не возвращаем само слово history, вместо этого снова запрашиваем ввод.
            continue

        # Если это не служебная команда, возвращаем введённую команду.
        # strip() удаляет лишние пробелы по краям.
        return value.strip()