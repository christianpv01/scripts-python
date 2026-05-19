'''Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib.request

url = 'http://www.pudim.com.br'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

req = urllib.request.Request(url, headers=headers)

try:
    resposta = urllib.request.urlopen(req)
except Exception as e:
    print(f'O site Pudim não está acessível no momento. ERRO: {e}')
else:
    print('Consegui acessar o site Pudim com sucesso!')