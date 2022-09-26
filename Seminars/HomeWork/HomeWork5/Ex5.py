# #1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# #'абвгдейка - это передача' = >" - это передача"

my_text = 'абвгдейка - это передача = >" - это передача"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)



# Задача №38: Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

# вариант человек против человека:
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")



# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

# Дополнительно(по желанию):
# 1 - Создайте программу для игры в ""Крестики-нолики"".
# 2 - Создать программу, считывающую два полинома из двух файлов и записывающая в третий файл их сумму.

#Функция создающая кортеж из двух равных списков  
def merge(list1, list2):

  list2_reg_up = [ch.upper() for ch in list2]#переводим текстовые строки списка в верхний регистр
  merged_list = tuple(zip(list1, list2_reg_up))#создаем кортеж 
  return merged_list

#Функция которая фильтрует список строк оставляя те номера строк, в суммах очков которых,
#содержится делитель совпадающий с порядовым номером соответствующей строки.
def divisor_matching(sum_of_points, number_of_elements):
  div_match  = []
  k = 0
  for i in sum_of_points:
    n = 1
    r = []
    while n <= i:
      if i % n == 0:
        r.append(n)
      n = n + 1
    for j in r:
      if j == number_of_elements[k]: 
        div_match.append(k)
    k = k + 1
  return div_match

#функция удаляющая из списка элементы не соответствующие условию функции divisor_maching
def del_elem_list(original_list, list_elements):
  modified_list = []
  for i in list_elements:
    for j in original_list:
      if original_list.index(j) == i: 
        #print(f'{j} = {i}')
        modified_list.append(j)
        break 
  return modified_list

#Открываем файл и считываем из него список названий языков программирования
names_list = open("c:/Users/Lenovo/Desktop/Developer Programmer/Python/Seminars"\
    "/HomeWork/HomeWork5/LangProg.txt", "r").read().splitlines()

#на основе списка из файла создаем список номеров строк 
number_of_elements = list(range (1,len(names_list)+1))

#на основе списков номеров и названий с помощью функции merged_list создаем кортеж 
merged_list = merge(number_of_elements, names_list)
print(merged_list)
print()

#из списка имен языков программирования создаем список сумм очков строк 
sum_of_points = []
for ch in names_list:
    sum_of_points.append(sum(ord(ch) for ch in ch))

#Перезаписываем измененные списки и формируем  конечный кортеж 
list_names = del_elem_list(names_list, divisor_matching(sum_of_points, number_of_elements))
list_points = del_elem_list(sum_of_points, divisor_matching(sum_of_points, number_of_elements))

merged_list2 = tuple(zip(list_points, list_names))
print(merged_list2)
