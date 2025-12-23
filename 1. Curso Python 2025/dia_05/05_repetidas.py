# %%

frases = {}

while True:
    frase = input('Digite uma frase: ')

    if not frase:
        break

    if frase in frases:
        frases[frase] += 1
    else:
        frases[frase] = 1

for chave, valor in frases.items():
    print('Contador:', valor, '-> Frase:', chave)