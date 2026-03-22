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
    else:
        for valor in enumerate(lista):
            if lista[n-1] > num:
                lista.append(num)
            else:
                lista.insert(n-1,num)
            print(n,valor)


'''    elif n == 1:
        if num > lista[0]:
            lista.append(num)
        else:
            lista.insert(0, num)
    elif n == 2:
        if num > lista[0]:
            lista.append(num)
        else:
            lista.insert()
    elif n == 3:
        if num > lista[0]:
            lista.append(num)
        else:        
            lista.insert()
    elif n == 4:
        if num > lista[0]:
            lista.append(num)
        else:        
            lista.insert()'''
print(lista)