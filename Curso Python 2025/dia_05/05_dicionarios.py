# %%

# PARES DE CHAVE/VALOR
martin = {
    'nome': 'Martin',
    'sobrenome': 'Schneider'
}

# %%

# PEGAR VALOR DE UMA CHAVE
print(martin['nome'])

# %%

# CRIANDO UMA CHAVE NOVA
martin['idade'] = 24
print(martin)

# %%

# RETORNAR TODAS AS CHAVES DO DICIONARIO
print(martin.keys())

# %%

# RETORNAR OS VALORES DE TODAS AS CHAVES
print(martin.values())

# %%

# TRAZER AS CHAVES E OS VALORES
print(martin.items())

# %%

# ACESSAR O VALOR DE TODAS AS CHAVES USANDO FOR
for i in martin:
    print(i, '->', martin[i])

# %%

# TAMBÉM PODEMOS ACESSAR O VALOR USANDO O ITEMS
for chave, valor in martin.items():
    print(chave, '->', valor)