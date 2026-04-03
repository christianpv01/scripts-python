'''
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
    de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) A média de idade do grupo.
    C) Uma lista com todas as mulheres.
    D) Uma lista com todas as pessoas com idade acima da média.
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
print(f'{'='*20} {cores["negativo"]}{'Desafio 94':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Grupo de pessoas.{cores['limpa']}\n')

cadastro = list()
totCAD = idadeSOMA = idadeMED = 0
print(f'{'~'*52}\n{'CADASTRO':^52}\n{'~'*52}\n')
while True:
    cad = dict()
    cad['Nome'] = str(input('Nome: ')).capitalize()
    cad['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    cad['Idade'] = int(input('Idade: '))
    cadastro.append(cad.copy())
    totCAD += 1
    idadeSOMA += cad['Idade']
    del cad
    verificador = str(input('Deseja cadastrar outra pessoa? [S/N] ')).strip().upper()[0]   
    if verificador in 'nN':
        print()
        break
    else:
        print(f'\n{'~'*52}')
idadeMED = idadeSOMA / totCAD
print(f'{'-'*52}\n{'RESULTADO':^52}\n{'-'*52}\n')
print(f'Foram cadastradas {totCAD} pessoas.')
print(f'A média de idade do grupo foi de {idadeMED:.2f}.')
print(f'{'_'*52}\n{'Lista de Mulheres':_^52}\n')
for m in range(0, totCAD):
    if cadastro[m]['Sexo'] == 'F':
        print(f'Nome: {cadastro[m]['Nome']}')
print(f'{'_'*52}\n{'Lista de idade':_^52}\n')
for m in range(0, totCAD):
    if idadeMED < cadastro[m]['Idade']:
        print(f'Nome: {cadastro[m]['Nome']} com {cadastro[m]['Idade']} anos.')
print(f'\n{'Fim do Programa':-^52}')