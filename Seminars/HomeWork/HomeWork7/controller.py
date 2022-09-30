from logger import save_data
from menu import title as hi
from actions import action as act
from actions import exit_from_app as exit
from view import *


def Calc_controll():
    hi()#приветствие
    while True:
        type = get_type() # задание типа переменной
        n1 = get_num1(type) # задание значения первого числа
        n2 = get_num2(type) # задание значения второго числа
        value_act = get_action()# задание действия над переменной
        result = act(value_act, n1, n2) # вычисление результата
        print(result)
        save_data(result, value_act, n1, n2) # сохранение данных
        view_data(result, value_act, n1, n2) # отбражение данных

        # выход из программы
        status = exit()
        if status: continue
        else: break