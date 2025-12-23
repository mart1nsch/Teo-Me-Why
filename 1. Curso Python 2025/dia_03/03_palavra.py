# %%
palavra = input('Digite uma palavra: ').lower()

tamanho_palavra = len(palavra)
contador = 0
contador_letra_a = 0

# USANDO WHILE
#while contador < tamanho_palavra:
#    if palavra[contador] == 'a':
#        contador_letra_a += 1
#    contador += 1

# USANDO FOR
for letra in palavra:
    if letra == 'a':
        contador_letra_a += 1

print('A letra "A" aparece', contador_letra_a, 'vez(es)')