'''
    Faça um programa que leia nome e média de um aluno,
    guardando também a situação em um dicionário.
    No final, mostre o conteúdo da estrutura na tela.
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
print(f'{'='*20} {cores["negativo"]}{'Desafio 90':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Aluno com média por dicionário.{cores['limpa']}')
print()

aluno = dict()
aluno['Nome:'] = str(input('Digite o nome do aluno: '))
aluno['Média:'] = float(input(f'Digite a média: '))
print(aluno)
print('-'*52)
for n, m in aluno.items():
    print(n, m)
print('-'*52)