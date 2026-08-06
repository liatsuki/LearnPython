n1 = input('N1: ')
n2 = input('N2: ')
n3 = int(input('N3: '))
n4 = int(input('N4: '))

print(type(n1))
print(type(n2))
print(type(n3))
print(type(n4))

s1 = n1 + n2
s2 = n3 + n4

print('A soma vale', s1)  # concatenacao
print('A soma vale', s2)  # soma

print('A soma entre {} e {} vale {}'.format(n3, n4, s2))
