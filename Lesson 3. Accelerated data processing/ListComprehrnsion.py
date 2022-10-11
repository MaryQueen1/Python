# list = []

# for i in range(1,101):
#     # if(i%2 ==0):
#         list.append(i)

# print(list)

# можно записать проще:

# list = [i for i in range(1,21)]
# print(list)

# list = [i for i in range(1,21) if i%2 ==0]
# print(list)

# список карежий (пар чисел):

# list = [(i, i) for i in range(1,21) if i%2 ==0]
# print(list)

# проделать операцию и прописать пару (число и его куб):

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1,21) if i%2 ==0]
# print(list)





# мой вариант задания:

# import os

# folder = r"C:\Users\DRUNK_ELEPHANT\Desktop\Queen\Getting to know Python\Lesson 3. Accelerated data processing\numbers.txt"
# path = os.path.dirname(folder)

# if not os.path.exists(path):
#     os.makedirs(path)

# with open(folder, 'w') as data:
#     data.write('1\n')
#     data.write('2\n')
#     data.write('3\n')
#     data.write('5\n')
#     data.write('8\n')
#     data.write('15\n')
#     data.write('23\n')
#     data.write('38\n')

# def f(x):
#     return x*x

# data = open(folder, 'r')
# dlist = [int(line.strip()) for line in data]
# data.close()

# list = [(i, f(i)) for i in dlist if i%2 ==0]

# print(list)



# другой вариант:

# path = r'C:\Users\DRUNK_ELEPHANT\Desktop\Queen\Getting to know Python\Lesson 3. Accelerated data processing\file.txt'

# f=open(path,'r')
# data=f.read()+' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data=data[space_pos+1:]

# out=[]
# for e in numbers:
#     if not e%2:
#         out.append((e,e**2))

# print(out)




# улучшенный вариант:
def select(f,col):
    return[f(x) for x in col]
    
def where(f,col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int,data)
res = where(lambda x: not x%2, res)
res = select(lambda x: (x,x**2),res)
print(res)

