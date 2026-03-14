'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
    Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 74':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Listagem de 5 números aleatórios.{cores['limpa']}')
print()


núm = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
print('Os números aleatórios da tupla são -> ',end='')
for c in range(0,5):
    print(núm[c],end=' ')
print()
print(f'O menor número da tupla é o {min(núm)}.')
print(f'O maior número da tuple é o {max(núm)}.')