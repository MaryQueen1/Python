# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Input quarter number: '))   

if quarter == 1:
    print('x > 0 and y > 0')
elif quarter == 2:
    print('x < 0 and y > 0')
elif quarter == 3:
    print('x < 0 and y < 0')
elif quarter == 4:
    print('x > 0 and y < 0')

else:
    print('Please, repeat the input (numbers 1, 2, 3 or 4')