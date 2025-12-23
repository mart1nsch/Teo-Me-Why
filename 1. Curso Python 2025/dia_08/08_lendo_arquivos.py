# %%

# ABAIXO É O JEITO MAIS RÚSTICO DE ABRIR UM ARQUIVO

nome_arquivo = 'historia.txt'

# ABRIR O ARQUIVO
open_file = open(nome_arquivo)

# %%

# LER O CONTEÚDO DENTRO
conteudo = open_file.read()

print(conteudo)

# %%

# FECHA O ARQUIVO
open_file.close()