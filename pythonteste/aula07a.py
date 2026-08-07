n1 = int(input('n1: '))
n2 = int(input('n2: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('=================================================')

print('Soma = {}'.format(s))
print('Produto = {}'.format(m))
print('Divisao = {:.3f}'.format(d))         # com apenas 3 casas decimais
print('Divisao inteira = {}'.format(di))
print('Potencia = {}'.format(e))

print('=================================================')

print('Soma = {}'.format(s), end=' ')
print('Produto = {}'.format(m), end=' ')
print('Divisao = {:.3f}'.format(d), end=' ')
print('Divisao inteira = {}'.format(di), end=' ')
print('Potencia = {}'.format(e))

print('=================================================')

print('Soma = {} \nProduto = {} \nDivisao = {:.3f}'.format(s, m, d))

print('=================================================')