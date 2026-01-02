# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')

# %%

# LIMPA AS LINHAS QUE TIVEREM AO MENOS UMA
# COLUNA COM NaN
df = df.dropna()

# %%

# ELIMINA A LINHA SOMENTE SE TODAS AS
# COLUNAS ESTIVEREM COM NaN
df = df.dropna(how='all')

# %%

# REMOVENDO SE TIVER EM CAMPO(S)
# ESPECIFICOS UM NaN (O ALL SIGNIFICA
# QUE PRECISA ESTAR EM TODOS OS CAMPOS
# DO SUBSET EM NaN)
df = df.dropna(how='all', subset=['DtCriacao', 'qtdePontos'])

# %%

# REMOVENDO SE TIVER EM UM DOS CAMPOS
# DO SUBSET, OU SEJA, COMO SE FOSSE UM
# OR, SE TIVER EM ALGUM DELES UM NaN, ELE
# IRÁ ELIMINAR A LINHA
df = df.dropna(how='any', subset=['DtCriacao', 'qtdePontos'])

# %%

# PEGA TODOS OS NaN DA COLUNA E COLOCA
# UM VALOR DEFINIDO
df = df['qtdePontos'].fillna(0)