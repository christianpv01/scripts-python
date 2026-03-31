'''
    Crie um programa que gerencie o aproveitamento de um jogador de futebol.
    O programa vai ler o nome do jogador e quantas partidas ele jogou.
    Depois vai ler a quantidade de gols feitos em cada partida. No final,
    tudo isso será guardado em um dicionário, incluindo o total de gols feitos
    durante o campeonato.    
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
print(f'{'='*20} {cores["negativo"]}{'Desafio 93':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Dados de jogadores.{cores['limpa']}')
print()

#Resolução 1

jogador = dict()
jogador['Nome'] = str(input('Nome do jogador: ')).capitalize()
jogador['Partidas'] = int(input('Nº de partidas: '))
jogador['Gols'] = int(input('Nº de gols: '))
saldoGOL = jogador['Gols'] / jogador['Partidas']
jogador['SaldoGOL'] = float(saldoGOL)
print(f'\n{'~'*52}\n{'|'}{' RAIO-X ':^50}{'|'}\n{'~'*52}\n')
print(f'O jogador {jogador['Nome']} atuou em {jogador['Partidas']} partidas.')
print(f'Com um total de {jogador['Gols']} e uma média de {jogador['SaldoGOL']:.2f}.')
print(f'\n{'~'*52}')

#Resolução 2

jog = dict()
gols = list()
totGols = 0
jog['Nome'] = str(input('Nome do jogador: ')).capitalize()
jog['Partidas'] = int(input(f'Quantas partidas {jog['Nome']} jogou? '))
for c in range(0, jog['Partidas']):
    n = int(input(f'Quantos gols na partida {c+1}? '))
    gols.append(n)
    totGols += n
jog['Gols'] = gols
jog['TotalGols'] = totGols
print(f'\n{'~'*52}\n{' RAIO-X ':^52}\n{'~'*52}\n')
print(f'O jogador {jog['Nome']} jogou {jog['Partidas']} partidas.')
for c in range(0, jog['Partidas']):
    print(f'    Na partida {c+1}, marcou {jog['Gols'][c]}.')
print(f'Marcando um total de {jog['TotalGols']}.')
print(f'\n{'~'*52}')