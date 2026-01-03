# %%

import pandas as pd

df = pd.read_csv('../data/produtos.csv', sep=';')
df

# %%

df.info()