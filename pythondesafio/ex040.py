# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida:
# - Media abaixo de 5.0: REPROVADO
# - Media entre 5.0 e 6.9: RECUPERACAO
# - Media 7.0 ou superior: APROVADO

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print('\033[0;32mAPROVADO\33[m')
elif media >= 5.0 and media <= 6.9:
    print('\033[0;33mRECUPERACAO\33[m')
else:
    print('\033[0;31mREPROVADO\33[m')