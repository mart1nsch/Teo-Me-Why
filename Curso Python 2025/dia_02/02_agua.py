# %%
print('Escolha uma das opcoes de agua:')
print('1. Agua sem gás')
print('2. Água com gás')

escolha = int(input())

print('Digite a quantidade de águas que voce quer: ')
quantidade = int(input())

if escolha == 1:
    preco_total = quantidade * 1.50
elif escolha == 2:
    preco_total = quantidade * 2.50

print('O preco total é:', preco_total)