# Faca um programa que leia pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo desse valor e ', type(a))
print('So tem espacos? ', a.isspace())
print('E um numero? ', a.isnumeric())
print('E alfabetico? ', a.isalpha())
print('E alfanumerico? ', a.isalnum())
print('Esta em maiusculas? ', a.isupper())
print('Esta em minusculas? ', a.islower())
print('Esta capitalizada? ', a.istitle())