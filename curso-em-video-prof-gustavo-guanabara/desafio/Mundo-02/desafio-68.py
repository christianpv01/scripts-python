'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
    mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

cores = {'limpa':'\033[m',
         'negativo':'\033[7m',
         'ciano_b':'\033[1;36m',
         'verde_b':'\033[1;32m',
         'vermelho_b':'\033[1;31m',
         'branco_fb':'\033[1;37;40m',
         'branco_s':'\033[4m',
         'amarelo_b':'\033[1;33m',
         'azul_b':'\033[1;34m',
         'roxo_b':'\033[1;35m'}
coresint = {1:'\033[1;36m',
            2:'\033[1;32m',
            3:'\033[1;31m',
            4:'\033[1;33m',
            5:'\033[1;34m',
            6:'\033[1;35m'}
from random import randint
from time import sleep
print(f'{'='*20} {cores["negativo"]}{'Desafio 68':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Par ou Ímpar usando break.{cores['limpa']}\n')

while True:
    parouimpar = {1:'PAR',2:'ÍMPAR'}
    escolhajog = 0   
    while escolhajog != 1 and escolhajog != 2: 
        escolhajog = int(input(' [1] PAR\n [2] ÍMPAR\n Escolha: '))
    if escolhajog == 1:
        escolhacomp = 2
    else:
        escolhacomp = 1
    print('-=' * 26)
    print(f' {coresint[randint(1,6)]}Jogador: {parouimpar[escolhajog]}\n {coresint[randint(1,6)]}Computador: {parouimpar[escolhacomp]}{cores["limpa"]}')
    print('-=' * 26)
    computador = randint(0,10)
    jogador = int(input(' Escolha seu número entre 0 a 10: '))
    soma = computador + jogador
    if soma % 2 == 0:
        resultado = 1
    else:
        resultado = 2
    cont = 0
    print(' Pensando',flush=True,end='')
    while cont <= 5:
        sleep(0.5)
        print('.',flush=True,end='')
        cont += 1
    print(f'\n O computador escolheu o número {computador}, somando {soma}.')
    if escolhajog == resultado:
        print(f' {cores["verde_b"]}VOCÊ GANHOU!!{cores["limpa"]}')
        print('~' * 52)
    else:
        print(f' {cores["vermelho_b"]}VOCÊ PERDEU!!{cores["limpa"]}')
        print('~' * 52)
        break