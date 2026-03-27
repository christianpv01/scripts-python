'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
    No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
    de cada aluno individualmente.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 89':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Boletim.{cores['limpa']}')
print()

boletim = list()
aluno = list()
média = totcad = 0
print(f'{cores["branco_fb"]}{'-'*52}\n{'CADASTRO DE ALUNOS':^52}\n{'-'*52}{cores["limpa"]}\n')
while True:
    aluno.append(str(input('            Nome: ')))
    for nota in range(0,2):
        aluno.append(float(input(f'            {nota+1}ª Nota: ')))
        média += aluno[nota+1]
        totcad += 1
    aluno.append(média/2)
    if média/2 >= 6:
        aluno.append('APROVADO')
    else:
        aluno.append('REPROVADO')
    boletim.append(aluno[:])
    aluno.clear()
    média = 0
    print(f'{' '*11}{'_'*29}')
    verificação = int(input(f'{' '*10}{'|'}{cores["negativo"]}{'MENU':_^29}{cores["limpa"]}{'|'}\n{cores["roxo_b"]}{'[1] Cadastrar Outro Boletim':^52}\n{'[2] Sair':^32}\n{'Escolha: ':>21}'))
    print(f'{cores["limpa"]}{' '*11}{'-'*29}')
    if verificação == 2:
        break
verificação = 0
while True:
    print('            Nomes:')
    for pos, c in enumerate(boletim):
        print(f'            {pos+1}. {boletim[pos][0]}')
    escolha = int(input('            Qual o nº do aluno\n            quer analisar? '))  
    if boletim[escolha-1][4] == 'APROVADO':
        print(f'{cores["verde_b"]}{'-'*52}\n{'BOLETIM':^52}\n{'-'*52}\n')
    else:
        print(f'{cores["vermelho_b"]}{'-'*52}\n{'BOLETIM':^52}\n{'-'*52}\n')
    print(f'Aluno: {boletim[escolha-1][0]}\n1ª Avaliação: {boletim[escolha-1][1]}\n2ª Avaliação: {boletim[escolha-1][2]}\nMédia: {boletim[escolha-1][3]}\n \nSituação do Aluno >> {boletim[escolha-1][4]}')
    print(f'{cores["limpa"]}')
    verificação = int(input(f'{' '*10}{'|'}{cores["negativo"]}{'MENU':_^29}{cores["limpa"]}{'|'}\n{cores["roxo_b"]}{'[1] Analisar Outro Boletim':^51}\n{'[2] Sair':^32}\n{'Escolha: ':>21}'))
    print(f'{cores["limpa"]}{' '*11}{'-'*29}')
    if verificação == 2:
        break