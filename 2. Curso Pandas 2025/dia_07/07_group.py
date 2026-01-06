# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df

# %%

# AGRUPA OS DADOS PELO IdCliente E FAZ UM COUNT
# EM CADA UMA DAS COLUNAS
df.groupby(by='IdCliente').count()

# %%

# AGRUPA OS DADOS PELO IdCliente E FAZ UM COUNT
# APENAS NA COLUNA ESPECIFICADA
df.groupby(by='IdCliente')['IdTransacao'].count()

# %%

# AGRUPA OS DADOS PELO IdCliente E FAZ UM COUNT
# NOS CAMPOS SELECIONADOS
df.groupby(by='IdCliente')[['IdTransacao', 'DtCriacao']].count()

# %%

# APLICANDO VÁRIOS TIPOS DE FUNÇÕES AGRUPADORAS
(df.groupby(by='IdCliente')
    .agg({
       'IdTransacao': ['count'],
       'QtdePontos': ['sum', 'mean']
   }))

# %%

# TIRAR A COLUNA AGRUPADORA PARA NÃO SER INDEX, SER
# CONSIDERADA COMO COLUNA
df.groupby(by='IdCliente', as_index=False)[['IdTransacao']].count()