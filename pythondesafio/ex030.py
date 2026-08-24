# Crie um programa que leia um numero inteiro e mostre na tela se ele e PAR ou IMPAR

num = int(input('Numero: '))

resul = num % 2

print('Resultado = {}'.format(resul))

if resul == 0:
    print('PAR (0)')
else:
    print('IMPAR (1)')