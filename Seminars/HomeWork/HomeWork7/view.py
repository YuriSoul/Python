
from menu import select_type_value as stv
from check import check_value_type as cvt
from check import check_num_real as cvr
from check import check_value_complex as cvc
from menu import example_action as ea
from check import check_action as ca

type_num = 0

#Ввод данных (получение данных от пользователя)

#Ввод типа переменной
def get_type():
    stv() # msg - выберите тип числа 
    while True:
        type_num = input(">> ")
        type_val = cvt(type_num) # проверка типа
        if 1 <= type_val <= 2:
            break
        else:
            continue
    return type_val

def get_num1(type):
    while True:
        num1 = int(input(f'Введите первое число: '))
        if type == 1:
            num1 = cvr(num1)
        else:
            num1 = cvc(num1)
        if num1 == False:
            continue
        else:
            break
    return num1

def get_num2(type):
    
    while True:
        num2 = int(input(f'Введите второе число: '))
        if type == 1:
            num2 = cvr(num2)
        else:
            num2 = cvc(num2)
        if num2 == False:
            continue
        else:
            break
    return num2


#Ввод действия
def get_action():
    ea()
    while True:
        val = input('Выберите действие: ')
        act = ca(val)
        if act == False:
            continue
        else:
            break
    return act

#Вывод данных (педставление данных пользователю (отобоажение данных на экране)
def view_data(res, act, n1, n2):
    print()
    print(f'result = {n1} {act} {n2} = {res}')
    print()


