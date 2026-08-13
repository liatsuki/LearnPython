# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porcao inteira
# Ex: Digite um numero: 6.127. O numero 6.127 tem a parte inteira 6.

from math import trunc

num_real = float(input('Numero real: '))
num_int = trunc(num_real)

print('O numero {} tem a parte inteira {}.'.format(num_real, num_int))

# ou 
# print('O numero {} tem a parte inteira {}.'.format(num_real, trunc(num_real)))
# print('O numero {} tem a parte inteira {}.'.format(num_real, int(num)))            -> sem necessidade de importar biblioteca