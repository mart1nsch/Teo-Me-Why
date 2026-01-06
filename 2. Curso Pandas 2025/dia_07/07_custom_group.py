# %%

import pandas as pd
import numpy as np

df = pd.read_csv('../data/transacoes.csv', sep=';')
df

# %%

# PODEMOS CRIAR MÉTODOS PARA USARMOS EM NOSSOS AGRUPAMENTOS
def  diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media) ** 2)

(df.groupby(by='IdCliente')
    .agg({
        'IdTransacao': ['count'],
        'QtdePontos': ['sum', 'mean', diff_amp]
    }))