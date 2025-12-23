# %%
print('Escolha o tipo de sorvete:')
print('1. Casquinha (R$1,00)')
print('2. Cascão (R$2,50)')
print('3. Cestinha (R$4,00)')

escolha_tipo = int(input())

print('Escolha o sabor:')
print('1. Morango')
print('2. Creme')
print('3. Chocolate')

escolha_sabor = int(input())

print('Escolha a cobertura:')
print('1. Caramelo (R$1,50)')
print('2. Morango (R$1,50)')
print('3. Chocolate (R$1,50)')
print('4. Sem cobertura (R$0,00)')

escolha_cobertura = int(input())

if escolha_tipo == 1:
    preco_total = 1
elif escolha_tipo == 2:
    preco_total = 2.50
elif escolha_tipo == 3:
    preco_total = 4

if escolha_cobertura >= 1 and escolha_cobertura <= 3:
    preco_total = preco_total + 1.50

print('O preco total é:', preco_total)