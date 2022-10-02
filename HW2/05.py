# Реализуйте алгоритм перемешивания списка.

import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Исходный список: ")
print(list)

def mix_list(list):
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list

mixed_list = mix_list(list)
print("Перемешанный список: ")
print(mixed_list)