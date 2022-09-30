#проверка рационального числа
def check_num_real(num):
    try:
        value = float(num)
        return num
    except:
        print('Некорректные данные')
        return False


#проверка типа значения
def check_value_type(type):
    try:
        chk_type = int(type)
        if 1 <= chk_type <= 2:
            return chk_type
        else:
            print('Некорректные данные')
        return False    
    except:
        print('Некорректные данные')
        return False

#проверка комплексного числа
def check_value_complex(val):
    try:
        value = complex(val)
        return value
    except:
        print('Некорректные данные')
        return False

#проверка действия
def check_action(act):
    if act == '*' or act == '/' or act == '+' or act == '-' or act == '^':
        return act
    else:
        print('Некорректные данные')
        return False