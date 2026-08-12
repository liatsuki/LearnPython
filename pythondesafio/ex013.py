# Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

salario = float(input('Salario: '))

novo_salario = salario + (salario * 15 / 100)
# aumento = salario * 0.15
# novo_salario = salario + aumento

print('Novo Salario = {:.2f}'.format(novo_salario))