# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# вариант записи. тот, что сверху не обязательно dataclose

# color = ['red', 'green', 'blue123']
# data = open('file.txt', 'a') # связываем с тект файлом
# # data.writelines(color) # передаем набор данных. разделителей не будет
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close() # обязательно


# exit() # позволяет не выполнять дальнейшие действия

path = 'file.txt'
data = open(path,'r')
for line in data:
    print(line)
data.close()