# %%

import pandas as pd

# %%

# CRIANDO DATA FRAME
df_clientes = pd.read_csv('../data/clientes.csv', sep=';')

# %%

# MOSTRA O NÚMERO DE LINHAS E COLUNAS
df_clientes.shape

# %%

# MOSTRA O NOME DAS COLUNAS
df_clientes.columns

# %%

# QUAIS SÃO OS INDICES
df_clientes.index

# %%

# MOSTRA OS TIPOS DAS COLUNAS
df_clientes.info()

# MOSTRA O USO DA MEMÓRIA RAM NO DETALHE
df_clientes.info(memory_usage='deep')

# %%

# RETORNA OS TIPOS DE CADA COLUNA APENAS (ELE RETORNA
# UMA SÉRIE, E O INDICE DA SÉRIE É O NOME DA COLUNA)
df_clientes.dtypes
df_clientes.dtypes['flEmail']