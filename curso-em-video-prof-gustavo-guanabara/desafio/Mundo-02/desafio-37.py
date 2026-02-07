'''Escreva um programa que leia um número inteiro qualquer e peça para
    o usuário escolher qual será a base de conversão:
    1 para binário
    2 para octal
    3 para hexodecimal'''
from time import sleep
layout = '='*20
cores = {'limpa':'\033[m',
         'verde_b':'\033[1;32m',
         'amarelo_b':'\033[1;33m',
         'azul_b':'\033[1;34m',
         'roxo_bf':'\033[1;45m'
         }
print('{} {}Desafio 37{} {}'.format(layout,cores['roxo_bf'],cores['limpa'],layout))
print(' Bases numéricas')
número = int(input(' Qual número deseja verificar? '))
print('')
verificador = int(input(' Agora escolha uma das opções:\n \n 1. Binário\n 2. Hexadecimal\n 3. Octal\n \n Escolha: '))
print('')
print(' Analisando . . .')
sleep(2)
print('')
if verificador == 1:
    print(' O número Binário de {} é {}{}{}.'.format(número,cores['amarelo_b'],bin(número),cores['limpa']))
elif verificador == 2:
    print(' O número Hexadecimal de {} é {}{}{}.'.format(número,cores['azul_b'],hex(número),cores['limpa']))
elif verificador == 3:
    print(' O número Octal de {} é {}{}{}.'.format(número,cores['verde_b'],oct(número),cores['limpa']))