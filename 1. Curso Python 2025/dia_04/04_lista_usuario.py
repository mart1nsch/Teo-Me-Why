# %%

lista = []

while True:
    valor = input('Digite um valor para a lista: ')

    if valor:
        lista.append(int(valor))
    else:
        break

print(lista)

numero = int(input('Digite o número a ser procurado: '))
contagem = 0

for i in lista:
    if i == numero:
        contagem += 1

print('Contagem:', contagem)