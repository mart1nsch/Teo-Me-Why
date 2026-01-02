# %%

# UMA MANEIRA DE DEFINIR LISTAS
idades = [24, 23, 18, 19, 59, 62]

# %%

# LISTAS PODEM TER QUALQUER TIPO DENTRO DELAS, TUDO MISTURADO
martin = ['Martin',
          'Schneider',
          24,
          'Masculino',
          5450.00,
          ['Karol', 'Alaire', 'Marcio', 'Carina']]

# %%

# PARA DESCOBRIR O TIPO DE UMA VARIÁVEL
print(type(martin))

# %%

# SOMAR TODAS AS IDADES DA LISTA
print(sum(idades))
# IDADE MINIMA
print(min(idades))
# IDADE MÁXIMA
print(max(idades))
# MÉDIA
print(sum(idades) / len(idades))

# %%

#PEGAR O ELEMENTO DO ÚLTIMO INDICE
print(martin[-1])

# %%

# PEGAR APENAS OS DOIS PRIMEIROS ELEMENTOS DA LISTA
print(martin[0:2])

# %%

# PEGAR OS ÚLTIMOS DOIS ELEMENTOS

print(martin[-2:])

# %%

# INVERTER A ORDEM DOS ELEMENTOS DE UM ARRAY
print(martin[::-1])

# %%

# FAZER UMA CÓPIA DA LISTA SEM COPIAR AS
# POSIÇÕES DA MEMÓRIA DA ORIGINAL
a = [1, 3, 6, 4]
b = a.copy()
b