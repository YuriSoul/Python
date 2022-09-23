
# 1 - Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

num = int(input('Введите число: '))
li = list(range(2, num))
liDiv = []
for i in li:
    if not num%i:
        if i > 1: 
            for j in range(2, int(i/2) + 1): 
                if(i % j) == 0: 
                    break 
            else: 
                liDiv.append(i) 
        else: 
            continue
print(liDiv)

# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список
#  неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from random import randint

numbers = []

for i in range(30):
    numbers.append(randint(0, 10))
print(numbers)

sortNumber = []
sortList = []
sortList.append(numbers[0])

def get_unique_numbers(numbers):
    unique = []

    for i in numbers:
        if i in unique:
            continue
        else:
            unique.append(i)
    return unique

sortNumber = get_unique_numbers(numbers)
print(sortNumber)
    



# 3 - В файле, содержащем фамилии студентов и их оценки, изменить
# на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.

# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

dicStudents = {} #создаем пустой словарь
#инициализируем словарь значениями
dicStudents = \
    {
        'Ангела Меркель': 5,
        'Андрей Валетов': 5,
        'Фредди Меркури': 3,
        'Анастасия Пономарева': 4
    }

#Создаем файл Students.txt и записываем в него наш словарь
with open('students.txt', 'w', encoding='utf-8') as data:
    for student, mark in dicStudents.items():
        data.write(f'{student}, {mark}\n')
    data.write('\n')
    data.close()    

with open('students.txt', 'a', encoding='utf-8') as data:
    for student, mark in dicStudents.items():
        if mark > 4:
            data.write(f'{student.upper()}, {mark}\n')
        else:
            data.write(f'{student}, {mark}\n') 
        #data.write(f'{student}, {mark}\n')
    data.close() 

# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов
#  влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" 
# можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования. 
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
#  а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


key = 2 # определение количества сдвигов
text = 'Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.'

print("Исходный текст: ", text)

#Функция шифратор - принимает текст, шифрует его и записывает в файл
def scrambler(text, key):
    encryption = ''
    for ch in text:
        if ch.isupper() and ch != ' ':
            # задаем положение буквы в алфавите 0-25
            ch_index = ord(ch) - ord("А")
            # выполнить смещение символа на задонное количество позиций
            new_index = (ch_index + key) % 32
            # преобразовываем в новый символ с учетом смещения
            new_unicode = new_index + ord("А")
            new_character = chr(new_unicode)
            #создаем зашифрованную строку из новых символов
            encryption = encryption + new_character
        #шифрование букв нижнего регистра
        elif ch.islower() and ch != ' ':
            ch_index = ord(ch) - ord("а")
            new_index = (ch_index + key) % 32
            new_unicode = new_index + ord("а")
            new_character = chr(new_unicode)
            encryption = encryption + new_character
        #добавление пробелов между словами
        else:
            encryption = encryption + ' '

    print('Текст зашифрован: ' + encryption)

    #Создаем файл EncodedFile.txt и записываем в него зашифрованный текст
    with open('EncodedFile.txt', 'w', encoding='utf-8') as data:
        for ch, in encryption:
            data.write(ch)
        data.close()
   
def decoder(text, key):
    decoding = ''   
     
    for ch in text:
        if ch.isupper() and ch != ' ':
            
            ch_index = ord(ch) - ord("А")
            
            new_index = (ch_index - key) % 32
            
            new_unicode = new_index + ord("А")
            new_character = chr(new_unicode)
            
            decoding = decoding + new_character
        
        elif ch.islower() and ch != ' ':
            ch_index = ord(ch) - ord("а")
            new_index = (ch_index - key) % 32
            new_unicode = new_index + ord("а")
            new_character = chr(new_unicode)
            decoding = decoding + new_character
        
        else:
            decoding = decoding + ' '
    print('Текст расшифрован: ', decoding)



scrambler(text, key)

key = int(input("Введите ключь чтобы разшифровать файл: "))

with open('EncodedFile.txt', 'r', encoding='utf-8') as data:
    text = data.read()
data.close()

decoder(text, key)


# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.
txt = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")

