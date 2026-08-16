# Crie um programa que leia o nome completo de uma pessoa e mostra:
    # - O nome com todas as letras maiusculas
    # - O nome com todas minusculas
    # - Quantas letras ao todo (sem considerar espacos)
    # - Quantas letras tem o primeiro nome

nome = str(input('Nome completo: ')).strip()  # para elimiar os espacos no inicio e fim

print('Em maiusculas = {}'.format(nome.upper()))
print('Em minusculas = {}'.format(nome.lower()))
print('Numero total de letras = {}'.format(len(nome) - nome.count(' ')))   # numero total de letras - numero de espacos
print('Numero de letras no primeiro nome = {}'.format(nome.find(' ')))  # diz a posicao do primeiro espaco = numero do nome

# ou
# dividido = nome.split()
# nome1 = dividido[1]
# print('Numero de letras no primeiro nome = {}'.format(len(nome1)))