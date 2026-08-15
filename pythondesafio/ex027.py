# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
    # Ex: Ana Maria de Souza
    # primeiro = Ana
    # ultimo = Souza

nome = input('Nome: ')

dividido = nome.split()
print('primeiro = {}'.format(dividido[0]))
print('ultimo = {}'.format(dividido[3]))