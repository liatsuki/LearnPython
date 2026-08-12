# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

n = float(input('Numero em metros: '))

km = n / 1000
hm = n / 100
dam = n / 10

dm = n * 10
cm = n * 100
mm = n * 1000

print('A medida de {:.1f}m corresponde a: '.format(n))
print(' -> {} km \n -> {} hm \n -> {} dam'.format(km, hm, dam))
print(' -> {} dm \n -> {:.0f} cm \n -> {:.0f} mm'.format(dm, cm, mm))