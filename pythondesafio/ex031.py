# Desenvolva um programa que pergunte a distancia de uma viagem em Km.
# Calcule o preco da passagem, cobrando 0,50 por Km para viagens de ate 200Km e 0,45 para viagens mais longas.

dist = float(input('Distancia da viagem: '))

print('Distancia = {:.1f}Km'.format(dist))

if dist <= 200:
    passagem = dist * 0.50
else:
    passagem = dist * 0.45

print('Preco da passagem = {:.2f} euros'.format(passagem))