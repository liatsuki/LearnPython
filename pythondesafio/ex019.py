# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

nome1 = str(input('Nome 1: '))
nome2 = str(input('Nome 2: '))
nome3 = str(input('Nome 3: '))
nome4 = str(input('Nome 4: '))

lista = [nome1, nome2, nome3, nome4]
aleatorio = random.choice(lista)

print('Nome aleatorio = {}'.format(aleatorio))