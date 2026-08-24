# Faca um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Numero: '))

suc = n + 1
ant = n - 1

print('\033[0;32mSucessor = {}\033[m'.format(suc))
print('\033[0;31mAntecessor = {}\033[m'.format(ant))

# OU
# print('Sucessor = {}'.format(n+1))
# print('Antecessor = {}'.format(n-1))