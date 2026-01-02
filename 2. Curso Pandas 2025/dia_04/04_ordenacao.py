# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')

# %%

# ORDENAMOS A SÉRIE DE PONTOS
df['qtdePontos'].sort_values()

# %%

# ORDENANDO O DF DO MENOR PARA MAIOR
df.sort_values(by='qtdePontos')

# %%

# ORDENANDO O DF DO MAIOR PARA O MENOR
df.sort_values(by='qtdePontos', ascending=False)

# %%

salarios = pd.DataFrame({
    'nome': ['Martin', 'Karol', 'Marcio', 'Alaire'],
    'idade': [24, 23, 59, 62],
    'salario': [5500, 5500, 3000, 3000]
})

# ORDENAÇÃO COM MAIS DE UM CAMPO
salarios.sort_values(by=['salario', 'idade'], ascending=[False, True])