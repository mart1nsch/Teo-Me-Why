# %%

import pandas as pd

# %%

# UMA SÉRIE É UMA LISTA, SÓ QUE NO PANDAS
series_idades = pd.Series([
    24,
    23,
    33,
    62,
    59
])
series_idades

# %%

# CALCULA A MÉDIA DA SÉRIE
series_idades.mean()

# %%

# SOMA TODA A SÉRIE
series_idades.sum()

# %%

# MÁXIMA DA SÉRIE
series_idades.max()

# %%

# VARIÁNCIA DA SÉRIE
series_idades.var()

# %%

# MOSTRA UM RESUMO DAS INFORMAÇÕES DA SÉRIE
series_idades.describe()