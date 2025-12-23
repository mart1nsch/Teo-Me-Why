# %%

nome_arquivo = 'historia.txt'

# ABRE O ARQUIVO POR MEIO DE UM 'LOOP', GARANTINDO QUE ELE SERÁ FECHADO,
# NÃO PRECISA DAR O COMANDO DO CLOSE
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
    print(conteudo)