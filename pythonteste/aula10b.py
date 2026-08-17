n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

m = (n1 + n2) / 2

print('Media = {:.1f}'.format(m))

if m>= 6.0:
    print('Sua media foi boa! PARABENS!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')