# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Nome: ')).strip()

print('Silva' in nome.lower())