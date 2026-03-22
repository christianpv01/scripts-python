'''Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, mostre
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma descrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 81':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Lista com vários números.{cores['limpa']}')
print()

lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    verificação = str(input(f'{'~'*15}Deseja continuar? [S/N] ')).lower().strip()[0]
    if verificação not in 'sS':
        break
print(f'{cores["amarelo_b"]}{'-'*52}')
print(f'{'RESULTADO':^52}')
print('-'*52)
#A) Quantos números foram digitados.
print(f'A lista contém {len(lista)} números.')

#B) A lista de valores, ordenada de forma descrescente.
lista.sort(reverse=True)
print(f'Lista decrescente: {lista}')

#C) Se o valor 5 foi digitado e está ou não na lista.
if lista.count(5) > 0:
    print(f'O valor 5 foi digitado {lista.count(5)} vez(es)')
else:
    print(f'O valor 5 não foi digitado.')

print(f'{'-'*52}{cores["limpa"]}')