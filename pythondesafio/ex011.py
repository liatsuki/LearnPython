# Faca um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua area e a quantidade de tinta necessaria para pinta-la, 
# sabendo que cada litro de tinta, pinta uma area de 2m2.

larg = float(input('Largura: '))
alt = float(input('Altura: '))

area = larg * alt
tinta = area / 2

print(' -> Sua parede tem a dimensão de {}x{} e a sua area é de {}m2.'.format(larg, alt, area))
print(' -> Para pintar essa parede, voce precisara de {} l de tinta.'.format(tinta))