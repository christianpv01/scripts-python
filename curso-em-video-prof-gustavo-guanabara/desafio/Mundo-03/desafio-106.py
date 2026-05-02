'''
Faça um nini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparece.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Obs: use cores.
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
         'roxo_b':'\033[1;35m',
         'azul_neg':'\033[7;34m',
         'verde_neg':'\033[7;32m'}
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
    print(f'{'='*20} {cores["negativo"]}{'Desafio 106':^}{cores["limpa"]} {'='*20}')
    print(f' {cores['branco_s']}Interactive Help com função.{cores['limpa']}\n')
    print(f'{'~'*52}\n{'H.E.L.P':^52}\n{'~'*52}')

def fim():
    print(f'\n{' FIM DO PROGRAMA ':-^52}\n{'-'*52}')

def interactivehelp():
    '''-> Bem vindo ao Interactive Help.
    Função para verificar o help da biblioteca ou função desejada.
    :param opção: digite a função ou biblioteca que deseja verificar.
    :param verificação: digite 1 para continuar a procurar outras funções/bibliotecas e 2 para finalizar.
    :return: mostra a função/biblioteca solicitada.
    '''
    while True:
        opção = str(input('Função ou Biblioteca >> '))
        t = " MANUAL DO COMANDO '{opção}' "
        f = '  PYTHON AJUDA  '
        print(f'{cores['negativo']}{'~'*len(t)}\n{t}\n{'~'*len(t)}{cores['limpa']}')
        print(cores['verde_b'])
        help(opção)
        print(cores['limpa'])
        while True:
            verificação = int(input(f'Deseja verificar outra Função ou Biblioteca?\n Sim [1]\n Não [2]\nEscolha: '))
            if verificação != 1 and verificação != 2:
                print('ERRO! Digite [1] para continuar ou [2] para finalizar.')
            else:
                print(f'{cores['azul_neg']}{'~'*len(f)}\n{f}\n{'~'*len(f)}{cores['limpa']}')
                break
        if verificação == 2:
            break

titulo()        
interactivehelp()
fim()