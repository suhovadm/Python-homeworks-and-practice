# 0.
# --- Ручной бэкап БД одной кнопкой! ---
def perform_backup():
    try:

        with open('IN.txt', 'r', encoding='utf8') as openBD, open('BACKUP.txt', 'w', encoding='utf8') as backupBD:
            for line in openBD:
                backupBD.write(line)
        print('[ База данных сохранена в файл BACKUP.txt ]')

    except FileNotFoundError:
        print('Извините, файл IN.txt не найден.')