# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

list = [random.uniform(1, 10) for i in range(0, 9)]
new_list = [round(i%1,2) for i in list if i%1 != 0]
result = max(new_list) - min(new_list)
print('\n', new_list)
print('\n',round(result, 3))
print()
