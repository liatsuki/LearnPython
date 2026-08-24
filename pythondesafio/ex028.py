# Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e 
# peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
# O programa devera escrever na tela se o usuario venceu ou perdeu.

from random import randint
from time import sleep # da um tempo ao computador para dar ideia de estar a processar

comp = randint(0, 5) # Da um numero aleatorio

print('-=-' * 20) # separador
print('Vou pensar em um numero entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)

jog = int(input('Em que número eu pensei? (0 a 5) '))

print('PROCESSANDO...')
sleep(3) # 3 segundos de espera

print('-=-' * 20)

if jog == comp:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}!'.format(comp, jog))