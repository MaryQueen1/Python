# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

list = [randint(1, 10) for i in range(1, 11)]
print(f"Исходный список: {list}")

new_list = []
[new_list.append(i) for i in list if i not in new_list]
print(f"Список из неповторяющихся элементов: {new_list}")

