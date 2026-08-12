# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

print('Media entre {:.1f} e {:.1f} = {:.1f}'.format(n1, n2, media))