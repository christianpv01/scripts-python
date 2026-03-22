'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
    já na posição correta de inserção(sem usar o sort()).
    No final mostre a lista ordenada na tela.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 80':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Lista sem utilizar o sort.{cores['limpa']}')
print()

lista = []
for n in range(0,5):
    num = int(input('Digite um número: '))
    if n == 0:
        lista.append(num)
    elif n == 1:
        if num > lista[0]:
            lista.append(num)
        else:
            lista.insert(0, num)
    elif n == 2:
        if num < lista[0]:
            lista.insert(0, num)
        elif num > lista[0] and num < lista[1]:
            lista.insert(1, num)
        else:
            lista.append(num)
    elif n == 3:
        if num < lista[0]:
            lista.insert(0, num)
        elif num < lista[1]:
            lista.insert(1, num)
        else:        
            lista.append(num)
    elif n == 4:
        if num < lista[1]:
            if num > lista[0] and num < lista[1]:
                lista.insert(1, num)
            else:
                lista.insert(0, num)
        elif num < lista[3]:
            if num > lista[2] and num < lista[3]:
                lista.insert(3, num)
            else:
                lista.insert(2, num)
        else:        
            lista.append(num)
print(f'Lista ordenada: {lista}')