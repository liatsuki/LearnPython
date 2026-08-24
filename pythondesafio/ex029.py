# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar 7.00 euros por cada Km acima do limite.

vel = float(input('Velocidade atual de um carro: '))

if vel > 80:
    multa = (vel - 80) * 7
    print('Multado! Voce excedeu o limite permitido que é de 80Km/h')
    print('Multa = {:.2f} euros'.format(multa))
else:
    print('Dentro do limite!')

print('Tenha um bom dia! Dirija com seguranca!')