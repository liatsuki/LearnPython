# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Numero: '))

d = n * 2         # dobro
t = n * 3         # triplo
r = n ** (1/2)    # raiz quadrada

print('Dobro = {} \nTriplo = {} \nRaiz quadrada = {:.2}'.format(d, t, r))

print('=== === === ===')

print('Raiz quadrada = {:.2}'.format(pow(n, (1/2)))) # funcao pow