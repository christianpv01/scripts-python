'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
    e que se encontram no intervalo de 1 até 500'''
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
print('{} {}Desafio 48{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Números ímpares entre 1 a 500, múltiplos de 3.{}\n'.format(cores['branco_s'],cores['limpa']))
soma = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
        print('{}{}'.format(coresint[randint(1,6)],c), end=' ')
print(cores['limpa'])
print('A soma dos números ímpares e múltiplos de 3 é de {}{}{}.'.format(cores['branco_s'],soma,cores['limpa']))