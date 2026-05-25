
# Escreva um programa que solicite ao usuário frases.
# Para para de solicitar frases, ele pode apenas apertar o "enter".
# Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.
# %%
# Solução via lista
frases = []
while True:
    frase = input('Digite uma frase: ')
    if bool(frase) is False:
        break
    frases.append(frase.title())

unico = sorted(set(frases))

for i in range(0,len(unico)):
    print(f'A frase "{unico[i]}" apareceu {frases.count(unico[i])} vez(es).')

# %%
# Solução via dicionário
dados = {}

while True:
    frase_dado = input('Entre com a frase: ')
    if frase_dado == '':
        break

    if frase_dado not in dados:
        dados[frase_dado] = 1
    else:
        dados[frase_dado] += 1

for i, j in dados.items():
    print(i, "->", j)

# %%
# Organizar em ordem decrescente via lambda (não funcionando ainda)
info = {
    'oi': 1,
    'ola': 10,
    'oi tudo bem': 3,
    'test': 2,
    'teste': 5,
}

items = list(info.items())
items.sort(key=lambda x: x[-1], reverse=True)

for i, j in items:
    print(i, '->', j)
# %%
