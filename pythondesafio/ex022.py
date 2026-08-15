# Crie um programa que leia o nome completo de uma pessoa e mostra:
    # - O nome com todas as letras maiusculas
    # - O nome com todas minusculas
    # - Quantas letras ao todo (sem considerar espacos)
    # - Quantas letras tem o primeiro nome

nome = input('Nome: ')

print(nome.upper())
print(nome.lower())

# print()

dividido = nome.split()
nome1 = dividido[1]
print(len(nome1))