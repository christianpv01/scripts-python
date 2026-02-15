'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''
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
print('{} {}Desafio 59{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Escolha 2 números e faça a opção.{}\n'.format(cores['branco_s'],cores['limpa']))
menu = 0
n1 = int(input(' 1º Número: '))
n2 = int(input(' 2º Número: '))
while menu != 5:
    print(' ========== MENU ==========')
    menu = int(input(' {}[1] Somar\n {}[2] Multiplicar\n {}[3] Maior\n {}[4] Novos Números\n {}[5] Sair do Programa\n {}Escolha: '.format(
        coresint[randint(1,6)],coresint[randint(1,6)],coresint[randint(1,6)],coresint[randint(1,6)],cores['vermelho_b'],cores['limpa']
    )))
    print('-'*25)
    if menu == 1:
        somar = n1 + n2
        print('O resultado da soma entre {} + {} = {}'.format(n1, n2, somar))
        print('-'*25)
    elif menu == 2:
        multiplicar = n1 * n2
        print('O produto de {} x {} = {}'.format(n1, n2, multiplicar))
        print('-'*25)
    elif menu == 3:
        maior = max(n1, n2)
        print('Entre os números {} e {} o maior deles é {}'.format(n1, n2, maior))
        print('-'*25)
    elif menu == 4:
        n1 = int(input(' 1º Número: '))
        n2 = int(input(' 2º Número: '))
    else:
        print('FIM')