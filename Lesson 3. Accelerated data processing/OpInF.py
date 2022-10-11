# def calc1(x):
#     return x+10

# def calc2(x):
#     return x*10

# def math(op,x):
#     print(op(x)) #op - операция, которую нужно будет провести

# math(calc2,10)




# def summ(x,y):
#     return x+y

# сейчас пропишу тоже самое , что и выше:

# sum = lambda x,y: x+y

# а еще можно положить в f = sum

def mylt(x,y):
    return x*y

def calc(op,a,b): #в качестве аргумента может быть целая функция
    print(op(a,b))
    #return op(a,b)

# calc(sum,4,5)

# можно убрать кусок кода и сделать таким образмом

calc(lambda x,y: x+y,4,5)
