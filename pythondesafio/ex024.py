# Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "SANTO"

cid = str(input("Cidade: ")).strip()

print(cid[:5].upper() == 'SANTO')