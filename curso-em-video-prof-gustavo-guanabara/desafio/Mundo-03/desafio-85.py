'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
    lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
    pares e ímpares em ordem crescente.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 85':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Lista Composta, verificação de pares e ímpares.{cores['limpa']}')
print()

lista = list()
par = list()
ímpar = list()
for n in range(0,7):
    núm = (int(input(f'Digite um número: ')))
    if núm % 2 == 0:
        par.append(núm)
    else:
        ímpar.append(núm)
par.sort()
ímpar.sort()
lista.append(ímpar[:])
lista.append(par[:])
lista.sort()
print(f'{cores["ciano_b"]}{'-'*52}\n{'LISTAS':^52}\n{'-'*52}')
print(f'>> Os números pares foram: {lista[1]}')
print(f'>> Os números ímpares foram: {lista[0]}')
print(f'{'-'*52}{cores["limpa"]}')