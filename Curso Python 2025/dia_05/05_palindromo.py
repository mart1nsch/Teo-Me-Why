# %%

palavra = input('Digite uma palavra: ')

invertida = palavra[::-1]

if palavra == invertida:
    print('É uma palavra palíndroma!')
else:
    print('Não é uma palavra palíndroma!')