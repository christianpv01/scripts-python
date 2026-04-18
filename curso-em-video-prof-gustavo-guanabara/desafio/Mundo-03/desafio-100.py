'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES
sorteados pela função anterior.
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
print(f'{'='*20} {cores["negativo"]}{'Desafio 100':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Sortear e SomaPar com função.{cores['limpa']}\n')

núm = list()
sPar = 0
def sorteia():
    print(f'Os valores sorteados são: ',end='')
    for c in range(0,5):
        núm.append(randint(0,10))
        print(núm[c],end=' ')
    print()

def somaPar(sPar):
    núm.sort()
    print(f'Pares: ',end='')
    for v in núm:
        if v % 2 == 0:
            print(v,end=' ')
            sPar += v
    print(f'\nSoma dos pares: {sPar}')

sorteia()
somaPar(sPar)
