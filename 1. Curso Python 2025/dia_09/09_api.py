# %%

import requests

url = 'https://viacep.com.br/ws/95166000/json/'

# %%

# FAZ A REQUISIÇÃO DA URL E RECEBE A RESPOSTA
resposta = requests.get(url)

# %%

# RESPOSTA DA API EM FORMATO JSON
dados = resposta.json()
print(dados)