'''
Crie um programa que tenha uma função chamata voto() que vai receber como parâmetro o
ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
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
print(f'{'='*20} {cores["negativo"]}{'Desafio 101':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Voto com função.{cores['limpa']}\n')

def titulo():
    print(f'{'~'*52}\n{'VERIFICADOR DE VOTAÇÃO':^52}\n{'~'*52}')

def voto():
    nascimento = int(input('Ano de nascimento: '))
    idade = (date.today().year) - nascimento
    print(f'Idade: {idade} anos.')
    if idade >= 18 and idade < 70:
        print(f'{cores["verde_b"]} >> Você está apto e pode votar{cores["limpa"]}') 
    elif ((idade >= 16) and (idade < 18)) or (idade >= 70):
        print(f'{cores["amarelo_b"]} >> O seu voto é opcional.{cores["limpa"]}')
    else:
        print(f'{cores["vermelho_b"]} >> Você ainda não pode votar!{cores["limpa"]}')

titulo()
voto()
print(f'\n{' FIM DO PROGRAMA ':-^52}\n{'-'*52}')