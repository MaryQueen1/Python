# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число: '))
array = range(1, N+1)
result = 1

print('[', end = ' ')
for i in array:
    result *= i
    print(result, end=' ')
print(']')