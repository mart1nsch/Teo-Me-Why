# %%

import pandas as pd

df = pd.read_excel('data/dados_cerveja_nota.xlsx')
df

# %%

from sklearn import tree

X = df[['cerveja']]
y = df['nota']

arvore_full = tree.DecisionTreeRegressor(random_state=42)
arvore_full.fit(X, y)

arvore_d2 = tree.DecisionTreeRegressor(random_state=42, max_depth=2)
arvore_d2.fit(X, y)

# %%

predict = arvore_full.predict(X.drop_duplicates())
predict_d2 = arvore_d2.predict(X.drop_duplicates())

# %%

import matplotlib.pyplot as plt

plt.plot(X['cerveja'], y, 'o')
plt.grid(True)
plt.title('Relação Cerveja vs Nota')
plt.xlabel('Cerveja')
plt.ylabel('Nota')

plt.plot(X.drop_duplicates()['cerveja'], predict)
plt.plot(X.drop_duplicates()['cerveja'], predict_d2)

plt.legend(['Observado', 'Árvore Full', 'Árvore Depth = 2'])