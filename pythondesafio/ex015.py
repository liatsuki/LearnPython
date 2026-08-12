# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a a pagar,
# sabendo que o carro custa 60 euros por dia e 0.15 km rodado.

km = float(input('Distancia percorrida: '))
dias = int(input('Dias alugados: '))

preco_dias = 60 * dias
preco_km = 0.15 * km
preco_total = preco_dias + preco_km

# ou
# formula = (60 * dias) + (0.15 * km)

print('Total = {:.2f}'.format(preco_total))