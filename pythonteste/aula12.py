nome = str(input('Nome: '))

if nome == 'Lidia':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Joao':
    print('Seu nome é bem popular em Portugal.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!'.format(nome))