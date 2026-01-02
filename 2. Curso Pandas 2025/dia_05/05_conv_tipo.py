# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')

# %%

# TRANSFORMANDO UM TIPO EM OUTRO - FLOAT
df['qtdePontos'].astype(float)

# %%

# PARA STRING
df['qtdePontos'].astype(str)

# %%

# CONVERTENDO UMA DATA STRING PARA DATETIME
pd.to_datetime(df['DtCriacao'])