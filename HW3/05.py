# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:

# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

n = int(input('Введите число: '))
list = [0]

def Fibonacci(i):
    if i in [1, 2]:                       
        return 1
    else:
        fib1, fib2 = 1, 1
        for j in range(2, i):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2

def NegaFibonacci(i):
    if i == 1:                       
        return 1
    elif i == 2:                       
        return -1
    else:
        fib1, fib2 = 1, -1
        for j in range(2, i):
            fib1, fib2 = fib2, fib1 - fib2
        return fib2

for i in range(1, n + 1):
    list.append(Fibonacci(i))
    list.insert(0, NegaFibonacci(i))
print(list)