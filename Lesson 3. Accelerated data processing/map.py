# li = [x for x in range(1,20)]

# li = list(map(lambda x: x+10,li))

# print (li)



# data = list(map(int,input().split()))
# print(data)



# data = map(int,input().split())

# for e in data:
#     print(e)


# data = map(int,'1 2 3'.split()) # если прописать так, то можно будет работать с map только один раз

# data = list(map(int,'1 2 3'.split())) # таким образом можно с этим работать несколько раз

# for e in data:
#     print(e)

# print('--')

# for e in data:
#     print(e)



# обработаем код из файла List...

def where(f,col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int,data) # избавляемся от функции select
res = where(lambda x: not x%2, res)
res = list(map(lambda x: (x,x**2),res)) # избавляемся от функции select
print(res)
