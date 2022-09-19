#1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

listNum = [5, 3, 1, 9, 7, 8, 4, 35, 44, 96]
print(listNum)
sumNum = 0

for i in listNum:
    print(f'{listNum.index(i)} - {i}')
    if (listNum.index(i)%2 != 0):
        sumNum += int(i)
print(sumNum)




#-Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]


listNums = [1, 2, 3, 4, 5, 6, 7]
print(listNums)
listProd = []
prodNum = 0

for i in listNums:
    if len(listNums)-listNums.index(i) >= i:
        prodNum = i*(len(listNums)-listNums.index(i))
        listProd.append(prodNum)
print(listProd)



#3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#между максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#[4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

import math
listNums = [1.1, 1.2, 3.1, 5.17, 10.02]
print(listNums)
listFractPart = []
max = 0
min = 1
difNum = 0

for i in listNums:
    listFractPart.append(round(math.fmod(i, 1.0), 2))

for i in listFractPart:
    if i > max:
        max = i
print(f'{max} -> {max}')

for i in listFractPart:
    if i < min:
        min = i
print(f'{min} -> {min}')

difNum = max - min
print(round(difNum, 2))


#4-Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Подумайте, как это можно решить с помощью рекурсии.
#Пример:

#45 -> 101101
#3 -> 11
#2 -> 10

s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)


#5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
            print(num2)
        return num2

list = [0]
userNumber = int(input('Enter any number: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)
