'''
Faça um programa que tenha uma função chamada maior(), que receba
vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles
é o maior.
'''
cores = {'limpa':'\033[m',                          #Dicionário de cores por string
         'negativo':'\033[7m',
         'ciano_b':'\033[1;36m',
         'verde_b':'\033[1;32m',
         'vermelho_b':'\033[1;31m',
         'branco_fb':'\033[1;37;40m',
         'branco_s':'\033[4m',
         'amarelo_b':'\033[1;33m',
         'azul_b':'\033[1;34m',
         'roxo_b':'\033[1;35m'}
coresint = {1:'\033[1;36m',                         #Dicionário de cores por inteiro
            2:'\033[1;32m',
            3:'\033[1;31m',
            4:'\033[1;33m',
            5:'\033[1;34m',
            6:'\033[1;35m'}
from random import randint
from time import sleep
from datetime import date
print(f'{'='*20} {cores["negativo"]}{'Desafio 99':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Maior com função.{cores['limpa']}\n')

def titulo():
    print(f'{'-'*52}\n{'Maior número':^52}\n{'-'*52}')

def fim():
    print(f'{'-'*52}\n{'-- FIM DO PROGRAMA --':^52}')    

def maior():
    núm = list()
    f = randint(0,10)
    for c in range(0,f):
        núm.append(randint(0,10))
    print(f'Foram informados {len(núm)} números.')
    print('São eles: ', end='')
    for pos, v in enumerate(núm):
        print(v, end=' ')
    print(f'\nO maior valor informado foi o {max(núm)}.')

titulo()
maior()
fim()