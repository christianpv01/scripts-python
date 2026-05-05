'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
à função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico.
Ex: n = leiaInt('Digite um n')
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

def titulo():
    print(f'{'='*20} {cores["negativo"]}{'Desafio 104':^}{cores["limpa"]} {'='*20}')
    print(f' {cores['branco_s']}Input com função.{cores['limpa']}\n')
    print(f'{'~'*52}\n{'FUNÇÃO INPUT':^52}\n{'~'*52}')

def fim():
    print(f'\n{' FIM DO PROGRAMA ':-^52}\n{'-'*52}')

def leiaInt(msg):
    '''-> Lê o número digitado, não aceitado dados diferentes de números.
    :param núm: O número a ser lido.
    :return: O número digitado.'''
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
           valor = int(n)
           ok = True
        else:
           print(f'{cores["vermelho_b"]}ERRO! O programa só aceita números inteiros.{cores["limpa"]}')
        if ok:
            break
    return valor


titulo()
número = leiaInt('Digite um número: ')
print(f' >> O número digitado, foi {número}.')
fim()