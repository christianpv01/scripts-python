'''
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
    sabendo que o vencedor tirou o maior número no dado.
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
from operator import itemgetter
print(f'{'='*20} {cores["negativo"]}{'Desafio 91':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Sorte nos dados.{cores['limpa']}')
print()

jogadores = {
            1: randint(1,6),
            2: randint(1,6),
            3: randint(1,6),
            4: randint(1,6)
            }
rank = list()

print(f'{coresint[randint(1,6)]} {f'_'*24} ')
print(f'{'|'}{'Sorteio':_^24}{'|'}')
print(f'{'|'}{f' '*24}{'|'}')
for k, v in jogadores.items():
    print(f'{'|'}{f'O {k}º jogador tirou {v}':^24}{'|'}')
print(f'{'|'}{f'_'*24}{'|'}{cores["limpa"]}')
print('')
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{cores["amarelo_b"]} {f'_'*24} ')
print(f'{'|'}{'Ranking':_^24}{'|'}')
print(f'{'|'}{f' '*24}{'|'}')
for c, i in enumerate(rank):
    print(f'{'|'}{f'{c+1}º Lugar: Jogador{i[0]} com {i[1]}|'}')        
print(f'{'|'}{f'_'*24}{'|'}{cores["limpa"]}')