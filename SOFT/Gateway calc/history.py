# Очередь истории и функции для добавления и отображения команд.

from config import HISTORY_LIMIT # Максимальное количество команд в истории.
from collections import deque # Очередь с ограничением кол-ва элементов.

# Создаём очередь для истории последних 100 введённых команд.
# Когда лимит превышен, самая старая запись удаляется автоматически.
history_list = deque(maxlen=HISTORY_LIMIT)

# Добавляем введённую пользователем строку в историю.
# Тип str означает, что ожидается текстовая строка.
def add_history_entry(command: str) -> None:
    history_list.append(command)

# Выводим историю введённых команд.
def show_history() -> None:
    print()

    # Если история пуста, сообщаем об этом.
    if not history_list:
        print("История пуста.")

    else:
        # Здесь вычисляем начальный номер записи.
        # Всего в истории будет храниться 100 элементов.
        start = max(0, len(history_list) - HISTORY_LIMIT)

        # enumerate() позволяет получить номер записи
        # и саму команду одновременно.
        for index, entry in enumerate(
            history_list, start=start + 1
        ):
            print(f"{index:3}. {entry}")

    print()