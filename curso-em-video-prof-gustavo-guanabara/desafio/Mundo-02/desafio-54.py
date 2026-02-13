'''Crie um programa que leia o ano de nascimento de sete pessoas.
    No final, mostre quantas pessoas ainda não atingiram a maioridade
    e quantas já são maiores.'''
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
from datetime import date
print('{} {}Desafio 54{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Verificação de Maior Idade.{}\n'.format(cores['branco_s'],cores['limpa']))
anoATUAL = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input(' Informe o {}º nascimento: '.format(c)))
    if (anoATUAL - nasc) >= 18:
        maior += 1
    else:
        menor += 1
print('\n Temos {} maiores de idade e {} menores.'.format(maior,menor))