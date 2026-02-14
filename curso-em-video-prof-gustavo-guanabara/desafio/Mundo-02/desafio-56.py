'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
    No final do programa, mostre:
    A média de idade do grupo.
    Qual é o nome do homem mais velho.
    Quantas mulheres têm menos de 20 anos.'''
layout = '='*20
cores = {'limpa':'\033[m',
         'negativo':'\033[7m',
         'ciano_b':'\033[1;36m',
         'verde_b':'\033[1;32m',
         'vermelho_b':'\033[1;31m',
         'branco_fb':'\033[1;37;40m',
         'branco_s':'\033[4m',
         'amarelo_b':'\033[1;33m',
         'azul_b':'\033[1;34m',
         'roxo_b':'\033[1;35m'
         }
coresint = {
         1:'\033[1;36m',
         2:'\033[1;32m',
         3:'\033[1;31m',
         4:'\033[1;33m',
         5:'\033[1;34m',
         6:'\033[1;35m'
         }
from random import randint
print('{} {}Desafio 56{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Cadastro de pessoas.{}\n'.format(cores['branco_s'],cores['limpa']))
idadeGRUPO = 0
F20 = 0
maisVELHO = 0
for c in range(1,5):
    print(coresint[randint(1,6)],end='')
    nome = str(input(' Qual o nome: '))
    idade = int(input(' Qual a idade: '))
    sexo = str(input(' Qual o sexo [M/F]: '))
    sexo = sexo.upper()
    print(cores['limpa'],end='')
    print('-='*12)
    idadeGRUPO += idade
    if sexo == 'F' and idade < 20:
        F20 += 1
    if sexo == 'M' and idade > maisVELHO:
        maisVELHO = idade
média = idadeGRUPO / 4
print(' A média de idade do grupo é de {:.1f} anos.'.format(média))
print(' O homem mais velho tem {}'.format(maisVELHO))
print(' Mulheres abaixo dos 20 anos: {}.'.format(F20))