'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela
    os n primeiros elementos de uma Sequência de Fibonacci'''
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
print('{} {}Desafio 63{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Sequência de Fibonacci.{}\n'.format(cores['branco_s'],cores['limpa']))

fb1 = 1
fb2 = 1
aux = 0
n = int(input('Até qual elemento deseja verificar: '))

while n != 0:
    print(' {}{}{}'.format(coresint[randint(1,6)],fb1,cores['limpa']),end='')
    n -= 1
    aux = fb2
    fb2 = fb1 + fb2
    fb1 = aux