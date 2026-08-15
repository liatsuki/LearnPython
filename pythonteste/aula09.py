frase = 'Curso em Video Python'

print(frase)

print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print('=== === === ===')

print(frase.count('o'))
print(frase.upper().count('O'))    # nao entendi
print(len(frase))
print(frase.replace('Python', 'Android'))    # para guardar - frase = print(frase.replace('Python', 'Android'))
print(frase.find('curso'))

print('=== === === ===')

print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])  # procurar no 'video' o espaco 3

print('=== === === ===')

print("""Roses are red,
Violets are blue,
Sugar is sweet,
And so are you.""")