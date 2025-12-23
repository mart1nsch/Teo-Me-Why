# %%
soma_total = 0

while True:
    valor = input('Digite um valor: ')
    
    if valor:
        valor = float(valor)
        soma_total += valor
    else:
        break

print('A soma total é:', soma_total)