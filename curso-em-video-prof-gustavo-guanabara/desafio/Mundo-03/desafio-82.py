'''Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, crie duas listas extras que vão conter apenas os valores
    pares e os valores ímpares digitados, respectivamente.
    Ao final, mostre o conteúdo das três listas gerada.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 82':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Listas de nºs Pares, Ímpares e total.{cores['limpa']}')
print()

lista = []
par = []
impar = []
while True:
    núm = int(input('Digite um número: '))
    lista.append(núm)
    if núm % 2 == 0:
        par.append(núm)
    else:
        impar.append(núm)
    verificação = str(input(f'{'~'*20} Deseja continuar? [S/N] ')).lower().strip()[0]
    if verificação not in 'sS':
        break
print(f'{cores["ciano_b"]}{'-'*52}')
print(f'{'RESULTADO':^52}')
print('-'*52)
print(f'Lista Principal  : {lista}')
print(f'Lista dos PARES  : {par}')
print(f'Lista dos ÍMPARES: {impar}')
print(f'{'-'*52}{cores["limpa"]}')