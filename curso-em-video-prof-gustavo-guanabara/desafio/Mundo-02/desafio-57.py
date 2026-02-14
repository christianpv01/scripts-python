'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
    Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
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
print('{} {}Desafio 57{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Verificação de Sexo.{}\n'.format(cores['branco_s'],cores['limpa']))
#Modelo 1
sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input(' Digite o sexo [M/F]: ')).upper()
print('Fim')
#Modelo 2
sexo = ''
while sexo not in ('F', 'M'):
    sexo = input('Digite o sexo [M/F]: ').upper()
print('Fim')