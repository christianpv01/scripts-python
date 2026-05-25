# %%
#nome_arquivo = 'test7.txt'

# Abre o arquivo, lê os dados e fecha o arquivo
#with open(nome_arquivo) as open_file:
#    conteudo = open_file.read()

#print(conteudo)

# %%
# Abre arquivo em formato de leitura
# open_file = open(nome_arquivo)

# Lê os dados do arquivo
# conteudo = open_file.read()
# print(conteudo)

# Fecha o arquivo
# open_file.close()

# %%

txt = 'Meu novo arquivo!'

nome_arquivo = 'test7_1.txt'

# w para escrever
with open(nome_arquivo, mode='w') as open_file:
    open_file.write(txt)

# %%

# a para adicionar
txt = 'Era uma vez..'
with open(nome_arquivo, mode='a') as open_file:
    open_file.write(txt)