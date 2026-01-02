# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')

# %%

# USANDO O REPLACE, TEMOS QUE PASSAR UM DICIONARIO
# ONDE A CHAVE É O VALOR ORIGINAL E O VALOR É O
# VALOR NOVO QUE IRÁ SER TROCADO
df['qtdePontos'] = df['qtdePontos'].replace({
    0: -1
})
df