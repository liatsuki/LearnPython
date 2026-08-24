print('\033[1;31;43mOla Mundo!\33[m')
print('\033[4;30;45mOla Mundo!\33[m')
print('\033[7;33;44mOla Mundo!\33[m')

nome = 'Lidia'
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {
    'limpa':'\033[m', 
    'azul':'\033[34m', 
    'amarelo':'\033[4;34m',
    'pretoebranco':'\033[7:30m'
}

nome = 'Maria'
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))