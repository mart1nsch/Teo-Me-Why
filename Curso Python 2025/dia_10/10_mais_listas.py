# %%

# PODEMOS CRIAR LISTAS UTILIZANDO CONDIÇÕES E LOOPS
numeros = [i for i in range(1, 101)]
print(numeros)

# %%

def eh_par(numero:int) -> bool:
    return numero % 2 == 0

numeros_pares = [i for i in range(1, 101) if eh_par(numero=i)]
print(numeros_pares)