# Faca um programa que leia uma frase pelo teclado e mostre:
    # Quantas vezes aparece a letra "A"
    # Em que posicao ela aparece a primeira vez
    # Em que posicao ela aparece a ultima vez

frase = str(input('Frase: ')).upper().strip()

print('Numero vezes que A aparece = {}'.format(frase.count('A')))
print('Posicao da primeira letra A = {}'.format(frase.find('A')+1))  # Para nao mostrar 0 ao utilizador
print('Posicao da ultima letra A = {}'.format(frase.rfind('A')+1))