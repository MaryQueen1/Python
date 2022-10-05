# # Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# # Пример:

# # 45 -> 101101
# # 3 -> 11
# # 2 -> 10

number = int(input('Введите число: '))
result = ''

if number == 2 or number == 4:
    while number >= 1:
        result = str(number % 2) + result
        number //= 2
else:
    while number >= 1:
        result = str(number % 2) + result
        number //= 2

print(result)


# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)