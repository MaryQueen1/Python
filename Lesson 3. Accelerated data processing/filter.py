#  пример работы filter

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2,data))
# print(res)


# обработаем код из файла map...

data = '1 2 3 5 8 15 23 38'.split()

res = map(int,data) # избавляемся от функции select
res = filter(lambda x: not x%2, res)
res = list(map(lambda x: (x,x**2),res)) # избавляемся от функции select
print(res)
