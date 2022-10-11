# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# # Входные и выходные данные хранятся в отдельных текстовых файлах.


# def rle(data):
#     encoding = '' # постепенно записываем результат
#     prev_char = '' # предыдущий символ
#     count = 1 # для счет кол-ва одинаковых букв

#     # if not data: return ''

#     for char in data:                                       #   для символа, который содержится
#         if char != prev_char:                               #      если символ не такой же как последний, то:
#             if prev_char:                                   #          если он является последним:
#                 encoding += str(count) + prev_char          #              к результату прибавить число и последний символ
#             count = 1                                       #          число становится 1
#             prev_char = char                                #          последний символ - это настоящий символ
#         else:                                               #      если такой же как "последний"
#             count+=1                                        #          увеличиваем число
#     else:                                                   #   если нет символов в файле
#         encoding +=str(count) +prev_char                    #   к результату прибавить число и последний символ
#         return encoding                                     #   возвращаем результат

# encoded_val = rle('AAAAbbRRRRTTllllwwdjffccc')
# print(encoded_val)


path = r'C:\Users\DRUNK_ELEPHANT\Desktop\Queen\Getting to know Python\HW5\without_rle.txt'
path2 = r'C:\Users\DRUNK_ELEPHANT\Desktop\Queen\Getting to know Python\HW5\with_rle.txt'

with open (path,'r') as data:
    without_rle = data.read()

def rle(text):
    prev_char = ''
    result = ''
    count = 1

    for char in text:
        if char != prev_char:
            if prev_char:
                result+=str(count)+prev_char
            count = 1
            prev_char = char
        else:
            count+=1
    else:
        result+=str(count)+prev_char
        return result

result = rle(without_rle)

with open (path2, 'w') as data2:
    data2.writelines(result)