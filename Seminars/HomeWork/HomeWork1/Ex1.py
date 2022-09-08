""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 
Пример: - 6 -> да - 7 -> да - 1 -> нет  """


def checkNumber(num):
    if 6 <= num <= 7:
        print("Это выходной")
    elif 0 < num < 6:
        print("Это будний")
    else:
        print("Это число не соответствует ни одному дню недели")

num = int(input("Введите число дня недели: "))
checkNumber(num) 


""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
для всех значений предикат.  """


def logical_statement(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
    print("Истинно")
else:
    print("Ложно")



'''Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
(или на какой оси она находится).

Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3'''

def inputKoord(x):
    a = [0] * x
    for i in range(x):
        number = float(input(f"Введите {i+1} координату: "))
        a[i] = number
    return a


def checkCoordinates(xy):
    if xy[0] > 0 and xy[1] == 0:
        text = "x"
    elif xy[0] == 0 and xy[1] > 0:
        text = "y"
    elif xy[0] < 0 and xy[1] == 0:
        text = "-x"
    elif xy[0] == 0 and xy[1] < 0:
        text = "-y"

    else: text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    
    if xy[0] == 0 or xy[1] == 0:
        print(f"Точка находится на оси {text}")
    else:
        print(f"Точка находится в {text} четверти плоскости")
    


koordinate = inputKoord(2)
checkCoordinates(koordinate)

'''Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
точек в этой четверти (x и y).'''

def checkQuarter(x):
    quarter = x
    if quarter == 1:
        text = "0 до (x)(y)"
    elif quarter == 2:
        text = "0 до (-x)(y)"
    elif quarter == 3:
        text = "0 до (-x)(-y)"
    elif quarter == 2:
        text = "0 до (x)(-y)"
    print(f"Диапазон возможных координат в {quarter} четверти от {text}")

    
numQuart = int(input("Введите номер четветри: "))    
checkQuarter(numQuart)


""" Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве. 
Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21 """


def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")