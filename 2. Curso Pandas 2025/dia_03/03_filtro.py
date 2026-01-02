# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')

# %%

# FAZEMOS UM FILTRO NUM DATA FRAME CRIANDO UMA
# SÉRIE DE BOOLEANOS INDICANDO QUAL REGISTRO
# IRÁ APARECER NO RETORNO E QUAL NÃO
filtro = df['QtdePontos'] >= 50
df[filtro]

# %%

# USANDO FILTRO COMPOSTO, TEMOS QUE USAR O & E
# COLOCAR CADA FILTRO ENTRE PARENTESES
filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] <= 100)
df[filtro]

# %%

# USANDO O OR
filtro = (df['QtdePontos'] == 50) | (df['QtdePontos'] == 100)
df[filtro]

# %%

# USANDO IN PARA ALGUM FILTRO
filtro = df['IdCliente'].isin(['9d023e72-c799-40c0-907a-96e023a97959', '1b08989c-039d-4c82-879b-0f56159a1ebb'])
df[filtro]

# %%

# USANDO BETWEEN
filtro = df['QtdePontos'].between(1, 50)
df[filtro]

# %%

# PARA USAR O NOT, USAMOS O ~
filtro = ~df['QtdePontos'].isin([1, 50])
df[filtro]