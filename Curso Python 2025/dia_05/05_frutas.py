# %%

frutas = {
    'Maça': 1.50,
    'Banana': 2.75,
    'Uva': 1.90,
    'Pera': 1.25,
    'Laranja': 0.65,
    'Limão': 1.25,
    'Goiaba': 2.15,
    'Abacaxi': 3.20,
    'Jaca': 5.80,
}

fruta = input('Escolha uma fruta: ')

if fruta in frutas:
    valor = frutas[fruta]
    print('O valor da fruta é R$', valor)
else:
    print('Fruta inválida')