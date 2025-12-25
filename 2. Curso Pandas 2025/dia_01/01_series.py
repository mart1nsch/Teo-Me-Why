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

# %%

# ORDENA DO MENOR PARA O MAIOR
print(series_idades.sort_values())
# PORÉM, O INDICE NÃO MUDA, MESMO MUDANDO A ORDEM,
# COMO PODEMOS VER, O PRIMEIRO ELEMENTO QUE APARECEU,
# ESTÁ COM O INDICE 1, E NÃO 0, O SEGUNDO É O 0,
# MANTER CUIDADO COM ISSO