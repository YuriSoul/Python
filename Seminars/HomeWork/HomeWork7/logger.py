#логирование работы программы
from datetime import datetime as dt


#сохранение логов
def save_data(res, act, x, y):
    time = dt.now().strftime("%Y/%m/%d, %H:%M")
    with open('log.csv', 'a') as file:
        file.write(f'{time}; {x}; {act}; {y}; {res}\n')
