# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите число: ')

def summ(number):
    if float(number) < 0:
        number = float(number) * (-1)
    result = 0

    for i in str(number):
        if i != '.':
            result += int(i)
    return result

print(f'Сумма числа равна {summ(number)}')

