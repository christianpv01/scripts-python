'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
#Utilizando o for
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
print('{} {}Desafio 60{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Consulta de fatorial.{}\n'.format(cores['branco_s'],cores['limpa']))
n = int(input(' Qual o Fatorial que gostaria de calcular? '))
f = 1
print()
for i in range(n,0,-1):
    print(f' {coresint[randint(1,6)]}{n}{cores["limpa"]}',end='')
    print(' x' if n > 1 else ' = ',end='')
    f *= n
    n -= 1
print(f'{coresint[randint(1,6)]}{f}{cores["limpa"]}\n')