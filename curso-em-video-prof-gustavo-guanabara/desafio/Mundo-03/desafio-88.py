'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
    O programa vai perguntar quantos jogos serão gerados e vai sortear
    6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 88':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Gerador de palpites.{cores['limpa']}')
print()

palpites = list()

jogos = int(input('Quantos jogos deseja sortear? '))
print()
for c in range(0, jogos):
    for count in range(0, 6):
        palpites.append(randint(1,60))
    print(f'{c+1}. Palpite: {palpites}')
    palpites.clear()
print()