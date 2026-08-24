# Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas/vindas de acordo com o valor.

print('\033[0;35m====== DESAFIO 02 ======\033[m')

nome = input('Nome: ')
print('Olá ' + nome + '! Prazer em te conhecer!')

print('Prazer em te conhecer, \033[4;33m{}\033[m!'.format(nome))