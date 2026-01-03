# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df

# %%

# FUNÇÃO QUE RETORNA O ÚLTIMO DADO DO
# ID DO CLIENTE
def get_last_id(x:str) -> str:
    return x.split('-')[-1]

# %%

# TRANSFORMANDO OS DADOS DO idCliente
# USANDO O APPLY E A FUNÇÃO CRIADA ACIMA
df['idCliente'] = df['idCliente'].apply(get_last_id)
df

# %%

# TRANSFORMA OS DADOS DA COLUNA PARA FLOAT
def int_to_float(x:int) -> float:
    return float(x)

df['qtdePontos'] = df['qtdePontos'].apply(int_to_float)
df

# %%

# APLICANDO O apply NAS LINHAS DE UM DATA FRAME
def verifica_pontos_twitch(linha) -> bool:
    return (linha['flTwitch'] > 0 and linha['qtdePontos'] > 500)

df['muitosPontosTwitch'] = df.apply(verifica_pontos_twitch, axis=1)
df