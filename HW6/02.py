# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их списком.

old = [1,2,3,4,5,6]

new = (list(map(lambda x: (1+1/x)**x, old)), 2)

print(new)