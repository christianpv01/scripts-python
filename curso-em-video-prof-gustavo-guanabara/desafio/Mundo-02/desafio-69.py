'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
    o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    A) Quantas pessoas tem mais de 18 anos.
    B) Quantos homens foram cadastrados.
    c) Quantas mulheres tem menos de 20 anos.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 69':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Cadastro de Pessoas usando break.{cores['limpa']}')
mais18 = homens = mulhermenos20 = 0
while True:
    print('=' * 52)
    idade = int(input(' Idade: '))    
    sexo = str(input(' Sexo [Masc/Fem]: ')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if idade < 20 and sexo == 'F':
        mulhermenos20 += 1
    if sexo == 'M':
        homens += 1
    verificação = str(input(' Deseja continuar [S/N]? ')).strip().upper()[0]
    if verificação == 'N':
        print('=' * 52)        
        break
print(f'\n{coresint[randint(1,6)]}{';~' * 26}')
print(f'\n{'Resultado':^52}\n')
print(f' Homem(ns) cadastrado(s): {homens}\n Pessoa(s) com mais de 18 anos: {mais18}\n Mulher(es) menor(es) de 20 anos: {mulhermenos20}\n')
print(f'{';~' * 26}{cores["limpa"]}\n')