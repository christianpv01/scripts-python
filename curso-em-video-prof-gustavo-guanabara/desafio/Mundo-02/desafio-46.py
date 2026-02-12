'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
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
print('{} {}Desafio 46{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Comemoração de ano novo{}\n'.format(cores['branco_s'],cores['limpa']))
from time import sleep
from emoji import emojize
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize(':fogos_de_artifício: :fogos_de_artifício: :fogos_de_artifício: {}Feliz ano novooo!!{} :fogos_de_artifício: :fogos_de_artifício: :fogos_de_artifício:'.format(cores['amarelo_b'],cores['limpa']), language='pt'))