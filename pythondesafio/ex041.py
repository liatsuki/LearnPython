# A Confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Ate 9 anos: MIRIM
# - Ate 14 anos: INFANTIL
# - Ate 19 anos: JUNIOR
# - Ate 20 anos: SENIOR
# - Acima: MASTER

from datetime import date

ano = int(input('Ano de nascimento: '))

idade = date.today().year - ano

if idade <= 9:
    print('MIRIM ({} anos)'.format(idade))
elif idade > 9 and idade <= 14:
    print('INFANTIL ({} anos)'.format(idade))
elif idade > 14 and idade <= 19:
    print('JUNIOR ({} anos)'.format(idade))
elif idade > 19 and idade <= 20:
    print('SENIOR ({} anos)'.format(idade))
else:
    print('MASTER ({} anos)'.format(idade))