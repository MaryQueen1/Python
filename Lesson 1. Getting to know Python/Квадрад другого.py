# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Примеры:

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

print('Введите первое число: ')
a = int(input())
print('Введите второе число: ')
b = int(input())

def square(a,b):
    if a * a == b:
        return 'Да'
    elif b * b == a:
        return 'Да25'
    else:
        return 'Нет'

print (square(a,b))

# Решение группы:

# a = int(input('Введите число a '))
# b = int(input('Введите число b '))

# if a*a==b:
#     print(f'- {a},{b} -> да')

# elif b*b==a:
#     print(f'- {a},{b} -> да')

# else:    
#     print(f'- {a},{b} -> нет')
