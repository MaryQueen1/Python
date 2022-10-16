name = ['Mary', 'Kit', 'Bro', 'Valya']
number = [1,2,3]

n_n = list(zip(name,number))
print(n_n)

n1, n2 = zip(*n_n)

print(n1)
print(n2)