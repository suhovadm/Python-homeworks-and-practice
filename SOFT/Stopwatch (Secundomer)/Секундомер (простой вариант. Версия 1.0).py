import time

while(True):
    print('Простой секундомер.')
    print('Нажмите Enter, чтобы запустить секундомер.')
    input()
    start_time = time.time()

    print('Секундомер запущен. Нажмите Enter, чтобы остановить.')
    input()
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f'Прошло времени: {elapsed_time:.2f} сек.\n')