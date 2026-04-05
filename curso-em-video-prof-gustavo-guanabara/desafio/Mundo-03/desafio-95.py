'''
    Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um
    sistema de visualização de detalhes do aproveitamento de cada jogador.
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
print(f'{'='*20} {cores["negativo"]}{'Desafio 95':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Jogadores.{cores['limpa']}\n')

gols = list()
jogador = dict()
jogadores = list()
jogCAD = saldoGOLS = aux = id = 0
while True:
    id += 1
    jogador['ID'] = id
    jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize()
    jogador['Partidas'] = int(input('Quantas partidas jogadas: '))
    for c in range(0, jogador['Partidas']):
        gols.append(int(input(f'Quantos gols na {c+1}ª partida: ')))
        saldoGOLS += gols[c]
    jogador['Gols'] = gols[:]   
    jogador['SG'] = saldoGOLS
    jogadores.append(jogador.copy())
    saldoGOLS = 0
    jogCAD += 1
    verificação = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if verificação in 'Nn':
        break
    elif verificação not in 'SsNn':
        print('Erro, favor escolher S ou N.')
        verificação = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    jogador.clear()
    gols.clear()
    print(f'{'-'*52}')
print(f'{'~'*52}\n{'Tabela de Jogadores':^52}\n{'~'*52}')
print(f'{'ID':^4}{'NOME':15}{'GOLS':24}{'TOTAL':^9}\n{'-'*52}')
for contador in range(0, jogCAD):
    aux = len(jogadores[contador]['Gols']*3)
    print(f'{jogadores[contador]['ID']:^4}{jogadores[contador]['Nome']:15}{jogadores[contador]['Gols']}{' '*(47-(aux+4+15))}{jogadores[contador]['SG']}')
print(f'{'-'*52}')
while True:
    dados = int(input(f'Qual jogador quer verificar? [ID] '))
    if dados == jogadores[dados-1]['ID']:
        print(f'\n{coresint[randint(1,5)]}Resultados do jogador: {jogadores[dados-1]['Nome']}.')
        for count in range(0, len(jogadores[dados-1]['Gols'])):
            print(f'{count+1}ª partida fez {jogadores[dados-1]['Gols'][count]} gol(s)')
        print(f'Total de gols: {jogadores[dados-1]['SG']}{cores["limpa"]}\n')
    else:
        dados = int(input(f'ID não cadastrado, favor informar um ID válido.\nQual jogador quer verificar? [ID] '))
    verificação = str(input('Deseja verificar outro jogador? [S/N] ')).strip().upper()[0]
    if verificação in 'Nn':
        break
    elif verificação not in 'SsNn':
        print('Erro, favor escolher S ou N.')
        verificação = str(input('Deseja verificar outro jogador? [S/N] ')).strip().upper()[0]    
    print(f'{'-'*52}')
print(f'{'-'*52}')