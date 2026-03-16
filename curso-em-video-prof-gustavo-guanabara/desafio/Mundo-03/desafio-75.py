'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 75':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Tuplas com 4 valores.{cores['limpa']}')
print()

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
tupla = (n1,n2,n3,n4)    
print()

#A) Quantas vezes apareceu o valor 9.
rep9 = 0
for c in range(0,len(tupla)):
    if tupla[c] == 9:
        rep9 += 1
print(f'O número 9 apareceu {rep9} vez(es).')
print()

#B) Em que posição foi digitado o primeiro valor 3.
for c in range(0,len(tupla)):
    if tupla[c] == 3:
        print(f'O número 3 apareceu na {c+1}ª posição.')
print()

#C) Quais foram os números pares.
for c in range(0,len(tupla)):
    if tupla[c] % 2 == 0:
        print(f'O número {tupla[c]} é PAR!')