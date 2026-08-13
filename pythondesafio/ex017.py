# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

c1 = float(input('Cateto 1: '))
c2 = float(input('Cateto 2: '))

h = hypot(c1, c2)

# ou
# h = sqrt((pow(c1,2) + pow(c2,2)))
# h = (c1 ** 2 + c2 ** 2) ** (1/2)

print('Hipotenusa = {:.2f}'.format(h))