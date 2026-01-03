# %%

import pandas as pd
import numpy as np

df = pd.read_csv('../data/clientes.csv', sep=';')
df

# %%

df['twitch_points'] = df['qtdePontos'] * df['flTwitch']
df

# %%

df['logPontos'] = np.log(df['qtdePontos'])
df

# %%

df['temRedeSocial'] = df['flTwitch'] + df['flYouTube'] + df['flBlueSky'] + df['flInstagram']
df

# %%

df = df.sort_values('qtdePontos', ascending=False)
maior = df.iloc[0]
menor = df.iloc[-1]
print('O com mais pontos é', maior['idCliente'], 'com', maior['qtdePontos'])
print('O com menos pontos é', menor['idCliente'], 'com', menor['qtdePontos'])

# %%

df = pd.read_csv('../data/transacoes.csv', sep=';')
df = df.sort_values('DtCriacao')
df['DtCriacao'] = pd.to_datetime(df['DtCriacao']).dt.date
df = df.drop_duplicates(subset=['IdCliente', 'DtCriacao'])
df