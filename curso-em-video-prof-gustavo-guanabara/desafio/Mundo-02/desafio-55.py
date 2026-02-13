'''Faça um programa que leia o peso de cinco pessoas.
    No final, mostre qual foi o maior e o menor peso lidos.'''
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
print('{} {}Desafio 55{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Verificação peso.{}\n'.format(cores['branco_s'],cores['limpa']))
maior = 0
menor = 1000
for c in range(1,6):
    peso = float(input(' {}. Informe o peso: '.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(' A pessoa mais pesada tem {:.2f}.\n A pessoa menos pesada tem {:.2f}.'.format(maior,menor))