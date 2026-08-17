# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar 7.00 euros por cada Km acima do limite.

vel = int(input('Velocidade de um carro: '))

if vel >= 80:
    cal = vel - 80
    multa = cal * 7
    print('Multado!')
    print('Multa = {} euros'.format(multa))
else:
    print('Dentro do limite!')