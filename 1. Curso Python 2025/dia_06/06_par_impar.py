# %%

def retorna_par_impar(num:int):
    if num % 2 == 0:
        return 'par'    
    return 'ímpar'

numero = int(input('Digite um número: '))

print('O número', numero, 'é', retorna_par_impar(numero))