# %%

import pandas as pd

idades = [24, 23, 33, 62, 59]
nomes = ['Martin', 'Karol', 'Carina', 'Alaire', 'Marcio']

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

# CRIA UM DATA FRAME VAZIO
df = pd.DataFrame()
print(df)

# %%

# CRIA UMA COLUNA NO DATA FRAME E ADICIONA A SERIE NELA
df['Idade'] = idades
print(df)

# %%

# CRIA UMA COLUNA NO DATA FRAME E ADICIONA A SERIE NELA
df['Nome'] = nomes
print(df)

# %%

# USAR O iloc[] PARA NAVEGAR ENTRE AS LINHAS DO DATA FRAME
print(df.iloc[0])

# %%

# PARA ACESSAR OS VALORES DE UMA COLUNA
print(df['Nome'])

# %%

# SE EU QUISER ACESSAR O NOME DO ÚLTIMO REGISTRO
print(df.iloc[-1]['Nome'])