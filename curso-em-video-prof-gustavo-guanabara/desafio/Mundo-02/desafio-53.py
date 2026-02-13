'''Crie um programa que leia um frase qualquer e diga se ela
    é um palíndromo, desconsiderando os espaços.'''
layout = '='*20
cores = {'limpa':'\033[m',
         'negativo':'\033[7m',
         'ciano_b':'\033[1;36m',
         'verde_b':'\033[1;32m',
         'vermelho_b':'\033[1;31m',
         'branco_fb':'\033[1;37;40m',
         'branco_s':'\033[4m',
         'amarelo_b':'\033[1;33m',
         'azul_b':'\033[1;34m',
         'roxo_b':'\033[1;35m'
         }
coresint = {
         1:'\033[1;36m',
         2:'\033[1;32m',
         3:'\033[1;31m',
         4:'\033[1;33m',
         5:'\033[1;34m',
         6:'\033[1;35m'
         }
from random import randint
print('{} {}Desafio 53{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Verificação de Palíndromo.{}\n'.format(cores['branco_s'],cores['limpa']))
frase = str(input(' Diga a palavra ou frase que deseja verificar: ')).lower()
frase1 = frase.replace(' ','')
fraselen = len(frase1)
frase2 = frase1[fraselen::-1]

if frase1 == frase2:
    print(' {}A palavra ou frase digitada é um PALÍNDROMO.{}'.format(cores['verde_b'],cores['limpa']))
else:
    print(' {}A palavra ou frase digitada NÃO é um palíndromo.{}'.format(cores['vermelho_b'],cores['limpa']))
