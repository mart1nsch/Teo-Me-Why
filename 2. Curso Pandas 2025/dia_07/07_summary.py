# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df

# %%

# PEGAR ALGUMAS COLUNAS E APLICAR UMA FUNÇÃO AGRUPADORA
campos = ['flEmail', 'flTwitch', 'flYouTube', 'flBlueSky', 'flInstagram']
df[campos].mean()