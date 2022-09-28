# #1- Определить, присутствует ли в заданном списке строк, некоторое число
n = 5
    
lst = ['uiu', 'adsgh', 'yuioilk', '15', 'dpo', '5']

def find_number(n, lst):
    return str(n) in lst

print(find_number(n, lst))


# #2-Найти сумму чисел списка стоящих на нечетной позиции
lst = [1, 2, 3, 4, 5, 6]

list_odd = list(filter(lambda x: x%2 != 0, lst))
print(list_odd)


# #3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)
import math

input_list = input("Введите координаты двух точек через пробел: ").split()
num_list = [int(i) for i in input_list]
print("Введенный список:", num_list)

distance = math.sqrt( ((num_list[0]-num_list[2])**2)+((num_list[1]-num_list[3])**2) )
print(distance)

# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


test_list = ["5", "asd", "zxc", "fjy", "asd"]
print(f"список: {test_list}")
test_item = input("Введите строку для поиска: ")


def check_list(test_list, test_item):
    count = 0
    for i in range(len(test_list)):
        if test_list[i] == test_item:
            count += 1
            if count == 2:
                print(count)
                return i
print(f"ответ: {check_list(test_list, test_item)}")


#5 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#	[2, 3, 4, 5, 6] => [12, 15, 16];
#	[2, 3, 5, 6] => [12, 15]

def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)

lst = [2, 3, 4, 5, 6]
mult_lst(lst)

# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def sequence(num):
        string = ''
        s = 1
        for i in list(range(num)):
                string = string + str(s) + ' '
                s *= -3
        return string

print(sequence(5))


