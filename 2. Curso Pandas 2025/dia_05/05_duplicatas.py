# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')

# %%

# REMOVE DUPLICATAS POR MEIO DE DEIXAR APENAS
# A PRIMEIRA, TODAS COLUNAS DEVEM SER IGUAIS
df.drop_duplicates()

# %%

# REMOVE DUPLICATAS POR MEIO DE DEIXAR APENAS
# A ÚLTIMA, TODAS COLUNAS DEVEM SER IGUAIS
df.drop_duplicates(keep='last')

# %%

# REMOVE APENAS QUANDO IGUAIS NOS CAMPOS
# INFORMADOS NO subset
df.drop_duplicates(subset=['flEmail', 'flTwitch'])

# %%

