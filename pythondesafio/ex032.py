# Faca um programa que leia um ano qualquer e mostre se ele e bissexto.

from datetime import date # pega a data de hoje

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year # pega a data de hoje, apenas ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano = {} -> BISSEXTO'.format(ano))
else:
    print('Ano = {} -> NAO BISSEXTO'.format(ano))