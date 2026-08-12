# Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto.

preco = float(input('Preco: '))

novo_preco = preco - (preco * 5 / 100)

# ou
# desconto = preco * 0.05
# novo_preco = preco - desconto

print('Preco com desconto = {:.2f}'.format(novo_preco))