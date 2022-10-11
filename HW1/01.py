# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Enter your number 1-7: '))

if(day==6 or day==7):
    print('Yes')

elif(day<1 or day>7):
    print('U must enter number from 1 to 7')

else:
    print('No')