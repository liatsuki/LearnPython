# Escreva um programa que converta uma temperatura digitada em C e converta para F.

c = float(input('Informe a temperatura em C: '))

f = ((c * 9) / 5) + 32

print('A temperatura de {} C corresponde a {} F!'.format(c, f))