'''
Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:
Quantidade de notas
A Maior nota
A Menor nota
A média da turma
A situação (opcional)
Adicione também as docstrings da função.
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
from math import factorial

def titulo():
    print(f'{'='*20} {cores["negativo"]}{'Desafio 105':^}{cores["limpa"]} {'='*20}')
    print(f' {cores['branco_s']}Notas com função.{cores['limpa']}\n')
    print(f'{'~'*52}\n{'TURMA 301-A':^52}\n{'~'*52}')

def fim():
    print(f'\n{' FIM DO PROGRAMA ':-^52}\n{'-'*52}')

def alunos():                                       #Função que cadastra aluno por aluno e suas notas, não faz parte do exercício.
    alunos = list()
    QtdAlunos = int(input('Quantos alunos vamos cadastrar? '))
    for c in range(0,QtdAlunos):
        aluno = dict()
        notas = list()
        totNotas = 0
        aluno['nome'] = str(input('Nome: ')).title()
        aluno['QtdNotas'] = int(input('Quantas provas você fez? '))
        for c in range(0,aluno['QtdNotas']):
            notas.append(round(float(input('Notas: ')),2))
        for c, pos in enumerate(notas):
            totNotas += pos
        aluno['notas'] = notas
        aluno['maior'] = max(notas)
        aluno['menor'] = min(notas)
        aluno['media'] = round(float(totNotas/aluno['QtdNotas']),2)
        if aluno['media'] >= 7:
            situação = 'APROVADO'
        else:
            situação = 'REPROVADO'
        aluno['situação'] = situação
        alunos.append(aluno)
        print('-'*52)

def notas(situação=False):
    '''-> Função para cadastrar notas dos alunos.
    :param QtdNotas: Validação de quantas notas serão cadastradas.
    :param Maior: Mostra a maior nota da turma.
    :param Menor: Mostra a menor nota da turma.
    :param Média: Mostra a média de notas.
    :param Situação: Mostra a situação da turma se está 'RUIM', 'REGULAR' ou 'BOA', para ativar informar (situação=True).
    :return: QtdNotas, Maior, Menor, Média, Situação(opcional)'''
    turma = dict()
    notas = list()
    totNotas = 0
    turma['QtdNotas'] = int(input('Quantas notas para cadastrar? '))
    for c in range(0, turma['QtdNotas']):
        notas.append(float(input(f'{c+1}ª Nota: ')))
        totNotas += notas[c]
    turma['maior'] = max(notas)
    turma['menor'] = min(notas)
    turma['média'] = round((totNotas/turma['QtdNotas']),2)
    turma['notas'] = notas.copy()
    if situação == True:
        if turma['média'] >= 7:
            turma['situação'] = 'BOA'
        elif turma['média'] >= 5:
            turma['situação'] = 'REGULAR'
        else:
            turma['situação'] = 'RUIM'
    print(turma)

titulo()
notas(situação=True)
fim()