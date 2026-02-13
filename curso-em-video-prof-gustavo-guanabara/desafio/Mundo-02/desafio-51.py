'''Desenvolva um programa que leia o primeiro termo e a razão
    de uma PA(progressão aritmética). No final, mostre os 10 primeiros termos dessa progressão.'''
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
print('{} {}Desafio 51{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Progressão Aritmética.{}\n'.format(cores['branco_s'],cores['limpa']))
termo1 = int(input(' Qual é o primeiro termo: '))
razão = int(input(' Qual é a razão: '))
for c in range(termo1,termo1+razão*10,razão):
    print('{}{}'.format(coresint[randint(1,6)],c),end=' ')
print('\n {}'.format(cores['limpa']))