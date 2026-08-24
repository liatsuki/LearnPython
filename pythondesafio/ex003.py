# Crie um script Python que leia dois numeros e tente mostrar a soma entre eles.

print('====== DESAFIO 03 ======')

n1 = int(input("Num 1: "))
n2 = int(input("Num 2: "))

s = n1 + n2

print('A soma entre \033[1;33m{}\033[m e \033[1;33m{}\033[m é igual a \033[1;32m{}\033[m!'.format(n1, n2, s))