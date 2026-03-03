'''Crie um programa que simule o funcionamento de um caixa eletrônico.
    No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
    e o programa vai informar quantas cédulas de cada valor serão entregues.
    OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 71':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Funcionamento de um caixa eletrônico.{cores['limpa']}')

print(f'{'=' * 52}\n{'MyBank':^52}\n{'=' * 52}')
print(f'{'Bem vindo ao meu, ao seu, ao nosso MyBank!':^52}\n')
saldo = randint(0,10000)                            #Saldo fictício entre 0 e 10000 apenas para teste
saque = deposito = n1 = n10 = n20 = n50 = n100 = 0  #Composição de variáveis
número_notas = {n1:randint(0,1000),                 #Dicionário número de notas utilizando randint
                n10:randint(0,100),
                n20:randint(0,50),
                n50:randint(0,20),
                n100:randint(0,10)}
dicionario_saque = {1:100,                          #Dicionário Saque
                    2:50,
                    3:20,
                    4:10,
                    5:1}
while True:
    verificador = int(input(' >>> O que deseja fazer?\n [1] Verificação de Saldo\n [2] Saque\n [3] Deposito\n [4] Sair\n Escolha: '))
    if verificador == 1:                            #Verifica o Saldo somente
        print(f'\n {cores["amarelo_b"]}>> Seu saldo é de R${saldo}{cores["limpa"]}')
        print()
    elif verificador == 2:                          #Abre a opção para saque
        print('-='*26)
        verificador_saque = int(input(' >>> Qual o valor que deseja sacar?\n [1] R$ 100\n [2] R$ 50\n [3] R$ 20\n [4] R$ 10\n [5] R$ 1\n [6] Outro valor\n Escolha: '))
        if verificador_saque == 6:
            saque = int(input(f'\n {cores["vermelho_b"]}>>> Digite o valor do saque: R$'))
        elif 0 < verificador_saque <= 5: 
            saque = dicionario_saque[verificador_saque]
        else:
            break
        if saldo < saque:
            print(f' {cores["vermelho_b"]}Valor indisponível para saque.{cores["limpa"]}')
            break
        else:
            if verificador_saque == 6:
                saldo -= saque
            elif 0 < verificador_saque <= 5:    
                saldo -= dicionario_saque[verificador_saque]
        if True:
            r100 = saque//100
            resto100 = saque % 100
            r50 = resto100//50
            resto50 = resto100 % 50
            r20 = resto50//20
            resto20 = resto50 % 20
            r10 = resto20//10
            resto10 = resto20 % 10
            r1 = resto10//1                
        print(f' {cores["vermelho_b"]}>>> Cédulas distribuidas:')
        if r100 != 0:
            print(f' >>> Notas de R$100: {r100}')
        if r50 != 0:
            print(f' >>> Notas de R$50: {r50}')
        if r20 != 0:
            print(f' >>> Notas de R$20: {r20}')
        if r10 != 0:
            print(f' >>> Notas de R$10: {r10}')
        if r1 != 0:
            print(f' >>> Notas de R$1: {r1}')                
        print(f' >>> Saldo atualizado: R${saldo}\n{cores["limpa"]}')
        print('-='*26)
    elif verificador == 3:                          #Abre a opção para deposito
        print('-='*26)
        deposito = int(input(f'{cores["verde_b"]}\n >>> Digite o valor para depósito: R$'))
        saldo += deposito
        print(f' >>> Saldo atualizado: R${saldo}\n{cores["limpa"]}')
        print('-='*26)
    else:                                           #Quebra o while
        break
print('-='*26)
print(f'\n {'Obrigado por utilizar nossos serviços.':^52}')
print(f'{'M Y B A N K':^52}\n')
print('=-'*26)