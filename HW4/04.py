# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите степень: '))
list = ''
polynom = r'C:\Users\Viole\OneDrive\python\HW4\polynom.txt'

for i in range(1, k+2):
    if k == 1:
        list += (f'{randint(1, 100)}*x + ')
    elif k == 0:
        list += (f'{randint(1, 100)+1}')
    else:
        list += (f'{randint(1, 100)}*x**{k} + ')
    k-=1


with open (polynom, 'w') as data:
    data.write(list)
    data.write(' = 0')