# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')

# %%

df.shape
df.info(memory_usage='deep')
df.dtypes

# %%

# TROCANDO O NOME DE UMA COLUNA
df = df.rename(columns={
    'IdTransacao': 'Id',
    'DescSistemaOrigem': 'Sistema'
})
df

# %%

# RETORNA OS VALORES DE UMA COLUNA (AQUI ELE SEMPRE VAI
# RETORNAR UMA SÉRIE)
df['IdCliente']

# %%

# RETORNA OS VALORES DE MAIS DE UMA COLUNA (AQUI ELE
# SEMPRE VAI RETORNAR UM DATA FRAME, MESMO QUE A LISTA
# TENHA APENAS UMA COLUNA INFORMADA)
df[['IdCliente', 'QtdePontos']]
df[['IdCliente']]

# %%

# SE EU QUISER MUDAR A ORDEM DAS COLUNAS, PARA,
# POR EXEMPLO, COLOCAR NA ORDEM ALFABETICA,
# PRIMEIRO NOS ORDENAMOS O ARRAY DOS NOMES DAS
# COLUNAS, E AI PASSAMOS ELE PARA O DATA FRAME
colunas = list(df.columns)
colunas.sort()
df[colunas]