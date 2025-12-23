# %%

def ola_mundo():
    print('eai mundo!')

ola_mundo()

# %%

# DEFINIÇÃO DE UMA FUNÇÃO, PODEMOS COLOCAR O TIPO NO PARÂMETRO,
# E O TIPO DO RETORNO TAMBÉM, PARA TUDO FICAR EXPLÍCITO
# A -> É O TIPO DO RETORNO, E O : DEPOIS DE x É O TIPO DO PARÂMETRO
def dobra(x:float) -> float:
    return x * 2

print(dobra(x=10))

# %%

def calcula_taxa_em_anos(valor:float, taxa:float, anos:int) -> float:
    return (valor + ((valor * (taxa / 100)) * anos))

print(calcula_taxa_em_anos(valor=1000, taxa=13, anos=5))

# %%

# TAMBÉM TEMOS OS PARÂMETROS OPCIONAIS, COLOCANDO O PARÂMETRO
# E APÓS UM VALOR PARA ELE, SEM DEFINIR O TIPO, ELES DEVEM SER
# OS ÚLTIMOS, SEMPRE APÓS OS OBRIGATÓRIOS

def multiplicador(numero:float, multiplicador=1) -> float:
    return numero * multiplicador

print(multiplicador(2, 3))

# SE EU NÃO MANDAR O PARÂMETRO, ELE PEGA O DEFAULT QUE DEFINI
print(multiplicador(2))

# %%

# TEMOS TAMBÉM UM PARÂMETRO QUE DEFINI QUE A FUNÇÃO ACEITA
# UM NÚMERO INFINITO DE PARÂMETROS, OU SEJA, 0 OU N
def soma(*args) -> float:
    valores = list(args)
    return sum(valores)

# NA CHAMADA DA FUNÇÃO, PODEMOS PASSAR QUANTOS PARÂMETROS QUISERMOS
print(soma(5, 4, 2, 2, 2))