'''Faça um programa que leia nome e peso de várias pessoas,
    guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 84':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Lista Composta, verificação de cadastro e peso.{cores['limpa']}')
print()

cadastro = []
dados = []
pesadas = []
leves = []
totcad = totpeso = totpesadas = totleves = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    cadastro.append(dados[:])
    totpeso += cadastro[totcad][1]
    dados.clear()
    totcad +=1
    verificação = str(input(f'{'~'*20} Deseja continuar? [S/N] ')).lower().strip()[0]
    if verificação not in 'Ss':
        break
print(f'{'-'*52}\n{'TABELA DE PESO':^52}\n{'-'*52}')
print(f'{cores["roxo_b"]}Foram cadastradas {totcad} pessoas.\nPesando no total de {totpeso}kgs.')   #A) Quantas pessoas foram cadastradas.
for p in cadastro:
    if p[1] > totpeso/totcad:
        pesadas.append(p)
        totpesadas += 1
    else:
        leves.append(p)
        totleves += 1
print(f'{cores["vermelho_b"]}\n>> As pessoas mais pesadas são: ')   #B) Uma listagem com as pessoas mais pesadas.
for c in pesadas:
    print(f'{c[0]} com {c[1]} kgs.')
print(f'{cores["verde_b"]}\n>> As pessoas mais leves são: ')   #C) Uma listagem com as pessoas mais leves.
for c in leves:
    print(f'{c[0]} com {c[1]} kgs.')
print(f'{cores["limpa"]}{'-'*52}')