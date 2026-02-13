'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
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
print('{} {}Desafio 52{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Número primo.{}\n'.format(cores['branco_s'],cores['limpa']))
número = int(input('Qual número deseja verificar? '))
print('\n {}Modelo 1'.format(cores['amarelo_b']))
if número == 2:
    print(' O número {} é um número primo.'.format(número))
elif número == 1:
    print(' O número {} NÃO é um número primo.'.format(número))
elif número % número == 0 and número % 1 == 0 and número % 2 != 0:
    print(' O número {} é um número primo.'.format(número))
else:
    print(' O número {} NÃO é um número primo.'.format(número))
print('\n {}Modelo 2\n Divisível por: '.format(cores['roxo_b']))
somaPRIMO = 0
for c in range(1,número+1):
    if número % c == 0:
        somaPRIMO += 1
        print(' {}'.format(c),end=' ')
if somaPRIMO == 2:
    print('\n O número {} é primo.{}'.format(número,cores['limpa']))
else:
    print('\n O número {} NÃO é primo.{}'.format(número,cores['limpa']))