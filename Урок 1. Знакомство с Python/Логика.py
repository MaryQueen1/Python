# a = 1 < 4
# print(a) #False

# f = 1 < 2 or 4 < 6
# print(f) #True (хотя бы одно высказывание истина)

x = [1,2,3,4]
# print(x)
# print(not 2 in x) #False (в списке не содержится 2)

# is_odd = x[0] % 2 == 0
# print(is_odd)

is_odd = not x[0] % 2
print(is_odd)