'''crie um programa que crie uma matriz de dimensão 3x3 e
    preencha com valores lidos pelo teclado.
    No final, mostre a matriz na tela, com a formatação correta'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 86':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Matriz 3x3.{cores['limpa']}')
print()

matriz = []
for c in range(0, 9):
    num = int(input('Digite um valor: '))
    matriz.append(num)
print(f'{coresint[randint(1,5)]}{'-'*52}\n{'MATRIZ':^52}\n{'-'*52}')
for c in range(0, 3):
    print(f'     [ {matriz[c]:3} ]',end='   ')
print()
for c in range(3, 6):
    print(f'     [ {matriz[c]:3} ]',end='   ')
print()
for c in range(6, 9):
    print(f'     [ {matriz[c]:3} ]',end='   ')
print(f'\n{'-'*52}{cores["limpa"]}')