'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
    que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
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
print('{} {}Desafio 50{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}SomaPAR{}\n'.format(cores['branco_s'],cores['limpa']))
somaPAR = 0
for c in range(1,7):
    núm = int(input('{}{}º Número: {}'.format(coresint[randint(1,6)],c,cores['limpa'])))
    if núm % 2 == 0:
        somaPAR += núm
print('{}A soma dos valores pares foi {}.{}'.format(cores['branco_s'],somaPAR,cores['limpa']))