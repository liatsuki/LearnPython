# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos won ela pode comprar.
# Considere 1.00€ = 1 635,62₩

euro = float(input('Em Euro: '))

won = euro * 1635.62
real = euro * 3.27

print('Conversao para Won = {:.2f}'.format(won))
print('Conversao para real = {:.2f}'.format(real))