#выполнение действий над числами

def action(act, n1, n2):
    if act == '+': return n1 + n2
    elif act == '-': return n1 - n2
    elif act == '*': return n1 * n2
    elif act == '/': return n1 / n2
    elif act == '^' and type(n1) != type(3-5j): return n1**n2 #(2i+5)
    else:
        return 'err'

#завершение программы
def exit_from_app():
    print('Для завершения работы введите(x) или нажмите Enter для продолжения')
    status = input()
    if status == '':
        return True
    else:
        return False

