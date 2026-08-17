# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
    # Ex: Ana Maria de Souza
    # primeiro = Ana
    # ultimo = Souza

nome = str(input('Nome completo: ')).strip()

dividido = nome.split()
print('primeiro nome = {}'.format(dividido[0]))
print('ultimo nome = {}'.format(dividido[len(dividido) - 1]))