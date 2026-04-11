'''Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''
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
print(f'{'='*20} {cores["negativo"]}{'Desafio 96':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Jogadores.{cores['limpa']}\n')

def titulo():
    print(f'{'-'*52}\n{'Área do Terreno':^52}\n{'-'*52}\n')

def área(largura, comprimento):
    print(f' >>> A área de um terreno de {largura} x {comprimento} é de {largura*comprimento} m².')
    
titulo()
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
área(largura,comprimento)