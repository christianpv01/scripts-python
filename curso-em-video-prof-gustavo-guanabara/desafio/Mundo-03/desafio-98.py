'''
Faça um programa que tenha uma função chamada contador()
que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada.
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
print(f'{'='*20} {cores["negativo"]}{'Desafio 98':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Contador com função.{cores['limpa']}\n')

def titulo():

    print(f'{'-'*52}\n{'Contagem':^52}\n{'-'*52}')

def contador():
    
    #A) De 1 até 10, de 1 em 1
    print('Contando de 1 até 10 de 1 em 1: ',end='',flush=True)
    for c in range(1,11):
        sleep(0.2)
        print(c, end=' ',flush=True)
    print()
    #B) De 10 até 0, de 2 em 2    
    print('Contando de 10 até 0 de 2 em 2: ',end='',flush=True)
    for c in range(10,-2, -2):
        sleep(0.2)
        print(c, end=' ',flush=True)
    print()
    #C) Uma contagem personalizada.
    print(f'{'~'*52}\nAgora é a sua vez, vamos tentar!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    while p == 0:
        print('ERRO! Valor do Passo não pode ser 0.')
        p = int(input('Passo: '))
    print(f'Contando de {i} até {f} de {p} em {p}: ',end='',flush=True)
    if i > f and p > 0:
        p *= -1
    if f % p == 0:
        f += p
    for c in range(i, f, p):
        sleep(0.2)
        print(c, end=' ', flush=True)
    print(f'\n{'~'*52}\n{'-- FIM DO PROGRAMA --':^52}')
titulo()
contador()