'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e o outro chamado show, que será um valor lógico(opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
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
from math import factorial
print(f'{'='*20} {cores["negativo"]}{'Desafio 102':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Fatorial com função.{cores['limpa']}\n')

def titulo():
    print(f'{'~'*52}\n{'FATORIAL':^52}\n{'~'*52}')

def fim():
    print(f'\n{' FIM DO PROGRAMA ':-^52}\n{'-'*52}')

def fatorial(núm, show=False):
    '''-> Calcula o Fatorial de um número.
    :param núm: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.'''

    if show == False:
        print(factorial(núm))
    else:
        n = núm
        for c in range(1,n+1):
            if n != 1:
                print(n,end=' x ')
            else:
                print(n,end=' = ')
            n -= 1
        print(factorial(núm))

titulo()
núm = int(input('Digite o número: '))
fatorial(núm, show=True)
fim()