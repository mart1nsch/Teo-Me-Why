# %%
contador = 1
somatoria_altura = 0

# USANDO WHILE
#while contador <= 4:
#    altura = float(input('Digite uma altura: '))
#    somatoria_altura += altura
#    contador += 1

# USANDO FOR
for i in range(4):
    altura = float(input('Digite uma altura: '))
    somatoria_altura += altura

print('A soma das alturas é:', somatoria_altura)