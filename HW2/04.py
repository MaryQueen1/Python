# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import os
from random import randint

N = int(input('Введите число больше 0: '))
product  = 1

array = [randint(-N, N) for i in range(-N, N + 1)]

folder = r"C:\Users\DRUNK_ELEPHANT\Desktop\Queen\Getting to know Python\HW2\positions.txt"
path = os.path.dirname(folder)

if not os.path.exists(path):
    os.makedirs(path)

folder2 = r"C:\Users\DRUNK_ELEPHANT\Desktop\Queen\Getting to know Python\HW2\array.txt"
path2 = os.path.dirname(folder2)

if not os.path.exists(path2):
    os.makedirs(path2)

with open(folder, 'w') as data:
    data.write('2\n')
    data.write('2\n')
    data.write('0\n')
    data.write('1\n')

data = open(folder2, 'w')
data.write(str(array))
data.close()

data = open(folder, 'r')
dlist = [int(line.strip()) for line in data]
data.close()

for i in dlist:
    product  *= array[i]

print(product)
print('Созданный массив из рандомных чисел можно посмотреть в папке array.txt')
print('Позиции чисел можно посмотреть в папке positions.txt')