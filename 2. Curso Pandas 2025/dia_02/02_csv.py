# %%

import pandas as pd

# IMPORTANDO CSV
df = pd.read_csv('../data/clientes.csv')
df

# %%

# SALVANDO UM DATA FRAME COMO CSV
df.to_csv('cleintes.csv')