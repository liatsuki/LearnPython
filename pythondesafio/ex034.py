# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento e de 15%.

salario = float(input('Salario do funcionario: '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100) # aumento de 10%
else:
    novo = salario + (salario * 10 / 100) # aumento de 15%

print('Salario anterior = {:.2f} euros'.format(salario))
print('Salario com aumento = {:.2f} euros'.format(novo))