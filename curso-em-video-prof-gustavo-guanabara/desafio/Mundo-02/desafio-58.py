'''Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10.
    Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
    palpites foram necessários para vencer.'''
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
print('{} {}Desafio 58{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Jogo da adivinhação.{}\n'.format(cores['branco_s'],cores['limpa']))
computador = 0
jogador = 11
totjogadas = 0
print(' Escolha um número entre 0 e 10.')
while computador != jogador:
    computador = randint(0,10)
    print('-' * 20)
    jogador = int(input(' Número: '))
    print('\n O computador jogou: {}'.format(computador))

    totjogadas += 1
if totjogadas == 1:
    print('-' * 20)
    print(' {}Foi necessário {} palpite para vencer!{}'.format(cores['vermelho_b'],totjogadas,cores['limpa']))
else:
    print('-' * 20)
    print(' {}Foram necessários {} palpites para vencer.{}'.format(cores['vermelho_b'],totjogadas,cores['limpa']))