'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente.
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
print(f'{'='*20} {cores["negativo"]}{'Desafio 103':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Ficha dos jogadores com função.{cores['limpa']}\n')

def titulo():
    print(f'{'~'*52}\n{'FICHA DO JOGADOR':^52}\n{'~'*52}')

def fim():
    print(f'\n{' FIM DO PROGRAMA ':-^52}\n{'-'*52}')

def ficha(nome='',gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f' >> O jogador {nome} fez {gols} gol(s).')

titulo()
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
ficha(nome,gols)
fim()