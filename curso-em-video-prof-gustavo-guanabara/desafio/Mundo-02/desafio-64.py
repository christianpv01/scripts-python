'''Crie um programa que leia vários números inteiros pelo teclado.
    O programa só vai parar quando o usuário digitar o valor 999,
    que é a condição de parada. No final, mostre quantos números
    foram digitadores e qual foi a soma entre eles (desconsiderando o flag).'''
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
print('{} {}Desafio 64{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Somador de inteiros.\n Caso queira parar, digite 999{}\n'.format(cores['branco_s'],cores['limpa']))
idade = 0
cont = 0
soma = 0
while idade != 999:
    idade = int(input(f' {coresint[randint(1,6)]}Digite um número: '))
    if idade != 999:
        cont += 1
        soma += idade
print(f'{coresint[randint(1,6)]} Foram digitados {cont} números e sua soma foi de {soma}.{cores["limpa"]}')