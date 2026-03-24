'''Aprimore o desafio 86, mostrando no final:
    A) A soma de todos os valores parece digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 87':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Matriz 3x3 v2.0.{cores['limpa']}')
print()

matriz = []
somapar = soma3c = maior2c = 0
for c in range(0, 9):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        somapar += num
    if c == 2 or c == 5 or c == 8:
        soma3c += num
    if 2 < c < 6:
        if maior2c < num:
            maior2c = num         
    matriz.append(num)
print()
print(f'{coresint[randint(1,5)]}{'-'*52}\n{'MATRIZ':^52}\n{'-'*52}')
for c in range(0, 3):
    print(f'     [ {matriz[c]:3} ]',end='   ')
print()
for c in range(3, 6):
    print(f'     [ {matriz[c]:3} ]',end='   ')
print()
for c in range(6, 9):
    print(f'     [ {matriz[c]:3} ]',end='   ')
print()
print(f'\n{'-'*52}\n')
print(f'A soma dos valores pares da matriz foi {somapar}')
print(f'A soma dos valores da terceira coluna foi {soma3c}')
print(f'O maior valor da segunda linha foi {maior2c}')
print(f'\n{'-'*52}{cores["limpa"]}')