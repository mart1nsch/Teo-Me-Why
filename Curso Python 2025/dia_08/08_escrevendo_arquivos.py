# %%

dado = 'Gustavo Braun é gay'

nome_arquivo = 'historia_02.txt'

# MODO SOMENTE ESCRITA, ELE IRÁ SOBREESCREVER TODO O ARQUIVO
with open(nome_arquivo, mode='w') as open_file:
    open_file.write(dado)

# %%

dado = '\nE o Roger Staudt também'

nome_arquivo = 'historia_02.txt'

# MODO SOMENTE ESCRITA ADICIONANDO O TEXTO AO FIM DO QUE
# JÁ ESTÁ NO ARQUIVO
with open(nome_arquivo, mode='a') as open_file:
    open_file.write(dado)