# %%
import requests  # para realizar requisições na web
import json      # para tratar listas/dicionarios para arquivos json
from tqdm import tqdm

import pandas as pd

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

url = 'https://viacep.com.br/ws/{cep}/json/'
dados = []
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:        # Requisição 200 (OK) é o código de resposta HTTP padrão que indica que sua requisição foi bem sucedida.
        dados.append(resposta.json())

dados
# %%

dataset = pd.DataFrame(dados)
dataset.to_csv('ceps.csv',sep=';')

# %%

with open('ceps.json', 'w', encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)