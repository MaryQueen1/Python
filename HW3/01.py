# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

list = [randint(1, 10) for i in range(1, 11)]
print('\nСписок из нескольких чисел:', list)

result = int(0)

for i in range(1,len(list),2):
    result += list[i]

print('\nCуммa элементов списка, стоящих на нечётной позиции:', result)
print()