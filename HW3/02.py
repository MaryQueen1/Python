# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

list = [randint(1, 10) for i in range(0, 9)]
print('\nСписок из нескольких чисел:', list)

number = len(list)
result = 1

print('Произведение пар чисел списка: [', end = ' ')

for i in range(len(list)):
    while i<len(list)/2 and number > len(list)/2:
        number -= 1
        result = list[i] * list[number]
        print(result, end = ' ')
        i+=1

print(']')
print()
