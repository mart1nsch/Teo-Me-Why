# %%

from random import randint

chances = 3
numero_sorteado = randint(1, 15)

def solicita_numero_usuario() -> int:
    while True:
        try:
            chute = int(input('Faça um chute de 1 até 15: '))
        except ValueError as err:
            print('Digite um número válido')
            continue
        
        if 1 <= chute <= 15:
            return chute

        print('Digite um número válido')

def valida_chute(chute:int, chance:int) -> bool:
    if chute == numero_sorteado:
        print('Parabéns, você acertou!')
        return True
    elif chance == (chances - 1):
        print('Fim de jogo, você perdeu!\nO número sorteado era', numero_sorteado)
    elif chute > numero_sorteado:
        print('Chute foi maior que o número')
    else:
        print('Chute foi menor que o número')
    
    return False

for i in range(chances):
    chute = solicita_numero_usuario()
    if valida_chute(chute, i):
        break