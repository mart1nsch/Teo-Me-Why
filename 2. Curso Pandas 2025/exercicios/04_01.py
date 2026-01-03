# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df

# %%

# Quantos clientes tem vínculo com a Twitch?
filtro = df['flTwitch'] == 1
len(df[filtro])

# %%

# Quantos clientes tem um saldo de pontos maior que 1000?
filtro = df['qtdePontos'] > 1000
len(df[filtro])

# %%

df = pd.read_csv('../data/transacoes.csv', sep=';')
df

# %%

# Quantas transações ocorreram no dia 2025-02-01?
data = pd.to_datetime('2025-02-01', format='%Y-%m-%d').date()
filtro = pd.to_datetime(df['DtCriacao']).dt.date == data
len(df[filtro])