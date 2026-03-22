'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
    Caso o número já exista lá dentro, ele não será adicionado.
    No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 79':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Lista sem números repetidos.{cores['limpa']}')
print()

lista = []
while True:
    numeros = int(input(f'{cores["limpa"]}{cores["roxo_b"]} >>Digite um número: '))
    if numeros not in lista:
        lista.append(numeros)
    verificação = str(input(f'{cores["limpa"]}{'~'*15} Deseja continuar? [S/N] ')).lower().strip()[0]
    if verificação not in 'sS':
        break
print(f'\n{'-' * 52}')
lista.sort()
print(f'{cores["limpa"]} A lista em ordem crescente: {coresint[randint(1,5)]}{lista}{cores["limpa"]}')
print('-' * 52)