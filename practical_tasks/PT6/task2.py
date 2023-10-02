import time

print('Нажмите ENTER для начала работы секундомера или CTRL+C для его остановки')

while 1:
    try:
        input()
        starttime = time.time()
        print('Секундомер начал работу')
        while 1:
            print('Текущее время: ', round(time.time() - starttime, 0), 'сек.', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('Секундомер стоп')
        endtime = time.time()
        print('Прошло:', round(endtime - starttime, 2),'сек.')
        break
