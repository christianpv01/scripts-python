'''Refaça o DESAFIO 009, mostrando a tabuada de um número
    que o usuário escolher, só que agora utilizando um laço for'''
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
print('{} {}Desafio 49{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Tabuada{}\n'.format(cores['branco_s'],cores['limpa']))
número = int(input('Escolha um número: '))
for c in range(1,11):
    print(' {}{} X {:>2} = {:>2}{}'.format(coresint[randint(1,6)],número,c,número*c,cores['limpa']))