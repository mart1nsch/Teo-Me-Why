# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df

# %%

# Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
redes_sociais = ['flTwitch', 'flYouTube', 'flBlueSky', 'flInstagram']
media = df[redes_sociais].mean().mean()
variancia = df[redes_sociais].var().var()
maximo = df[redes_sociais].max().max()
print('Média:', media)
print('Variancia:', variancia)
print('Máximo:', maximo)

# %%

df = pd.read_csv('../data/transacoes.csv', sep=';')
df

# %%

# Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.
(df.groupby(by='IdCliente', as_index=False)[['IdTransacao']]
 .count()
 .sort_values('IdTransacao', ascending=False)
 .head(10))

# %%

# Qual usuário teve maior quantidade de pontos debitados
(df.groupby(by='IdCliente', as_index=False)[['QtdePontos']]
 .sum()
 .sort_values('QtdePontos', ascending=False)
 .iloc[0]
 ['IdCliente'])

# %%

# Qual a média de transações / dia?
df['DtCriacao'] = pd.to_datetime(df['DtCriacao']).dt.date
(df.groupby(by='DtCriacao', as_index=False)[['IdTransacao']]
 .count()
 ['IdTransacao']
 .mean())

# %%

# Quem teve mais transações de Streak?
transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacao_produto = pd.read_csv('../data/transacao_produto.csv', sep=';')
produtos = pd.read_csv('../data/produtos.csv', sep=';')
#produtos = produtos[produtos['DescNomeProduto'] == 'Presença Streak']
produtos

# %%

transacoes_streak = transacao_produto[transacao_produto['IdProduto'] == 12]
transacoes_streak