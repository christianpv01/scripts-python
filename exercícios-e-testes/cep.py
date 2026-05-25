# %%
import requests

ceps = [
    '25085132',
    '01001000',
    '20040002',
    '30140071',
    '40010000',
    '50030000',
    '60060120',
    '70040900',
    '80010000',
    '88010020',
    '90010000'
]
dicionario = dict()
for i in range(len(ceps)):
    url = 'https://viacep.com.br/ws/' + ceps[i] + '/json/'
    print(url)
    resposta = requests.get(url)
    dados = resposta.json()
    dicionario[ceps[i]] = dados

# %%

print(dicionario.items())