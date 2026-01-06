# %%

import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
clientes = pd.read_csv('../data/clientes.csv', sep=';')


# %%
transacoes
# %%
clientes

# %%

# LIGA OS DOIS DATA FRAMES INDO DO TRANSACOES PARA O CLIENTES
transacoes.merge(clientes,
                 left_on='IdCliente',
                 right_on='idCliente',
                 how='inner')

# %%

# PODEMOS MUDAR O NOME DAS COLUNAS REPETIDAS USANDO suffixes
transacoes.merge(clientes,
                 left_on='IdCliente',
                 right_on='idCliente',
                 how='inner',
                 suffixes=['Transacao', 'Cliente'])

# %%

# PODEMOS USAR OUTROS TIPOS DE JOINS, COMO O left
transacoes.merge(clientes,
                 left_on='IdCliente',
                 right_on='idCliente',
                 how='left',
                 suffixes=['Transacao', 'Cliente'])