# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos.
# Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

nome1 = str(input('Nome 1: '))
nome2 = str(input('Nome 2: '))
nome3 = str(input('Nome 3: '))
nome4 = str(input('Nome 4: '))

lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)

print('Ordem = {}'.format(lista))