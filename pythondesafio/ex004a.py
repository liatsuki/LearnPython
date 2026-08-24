# Crie um script Python que leia o dia, o mes e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

print('====== DESAFIO 04a ======')

dia = input('Dia: ')
mes = input('Mes: ')
ano = input('Ano: ')

print('Voce nasceu no dia \033[1;35m{}\033[m de \033[1;33m{}\033[m de \033[1;32m{}\033[m. Correto?'.format(dia, mes, ano))