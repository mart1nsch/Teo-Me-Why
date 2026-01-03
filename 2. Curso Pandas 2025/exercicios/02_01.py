# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df

# %%

df['valores'] = 1
df

# %%

df.to_csv('transacoes_1.csv')