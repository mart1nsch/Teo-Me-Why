# %%

import requests
import json
# ESSE TQDM SERVE PARA MOSTRAR BARRA DE PROGRESSO
from tqdm import tqdm

arquivo_ceps = 'ceps.json'

ceps = [
    '93950000',
    '95166000'
]

url = 'https://viacep.com.br/ws/{cep}/json/'

dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))

    if resposta.status_code == 200:
        dados.append(resposta.json())
    else:
        print('Houve uma falha na requisição:', resposta.status_code)
        break

with open(arquivo_ceps, mode='w', encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)