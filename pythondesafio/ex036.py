# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

valor_casa = int(input('Valor da casa: '))
salario = int(input('Salario do comprador: '))
anos = int(input('Quantos anos vai pagar: '))

prest_mensal = valor_casa / (anos * 12)
limite = salario * 0.30

if prest_mensal <= limite:
    print('\033[0;32mEmprestimo Aprovado\33[m')
else:
    print('\033[0;31mEmprestimo Negado\33[m')