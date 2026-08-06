# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele.

print('====== DESAFIO 04 ======')

p = input('Palavra: ')

print('O tipo primitivo desse valor é {}'.format(type(p)))

print('Só tem espacos? ', p.isspace())
print('É um número? ', p.isnumeric())
print('É alfabético? ', p.isalpha())
print('É alfanumérico? ', p.isalnum())
print('Está em maiúsculas? ', p.isupper())
print('Está em minúsculas? ', p.islower())
print('Está capitalizada? ', p.istitle())

