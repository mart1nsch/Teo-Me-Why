# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')

# %%

# MODIFICANDO OS DADOS DE UMA COLUNA
df['qtdePontos'] += 100
df

# %%

# CRIANDO UMA NOVA COLUNA NO DF
df['pontosDobrados'] = df['qtdePontos'] * 2
df