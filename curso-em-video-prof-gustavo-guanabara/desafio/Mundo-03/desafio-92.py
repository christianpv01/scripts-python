'''
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
    em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
    contratação e o salário. Calcule e acrescente, Além da idade, com quantos anos a pessoa vai se aposentar.
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
print(f'{'='*20} {cores["negativo"]}{'Desafio 92':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Calculo da aposentadoria.{cores['limpa']}')
print()
anoatual = date.today().year
print(f'{'-'*52}\n{' FICHA CADASTRAL ':-^52}\n{'-'*52}\n')
aux = dict()
cadastro = list()
aux['Nome'] = str(input('Nome: ')).capitalize()
aux['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
aux['Nascimento'] = int(input('Nascimento(Ano): '))
aux['Idade'] = int(anoatual-aux['Nascimento'])
perg = str(input('Possui Carteira de trabalho? [S/N] ')).strip().upper()[0]
if perg in 'Ss':
    aux['CTPS'] = str(input('Carteira de Trabalho: '))
    aux['Contratação'] = int(input('Ano de contratação: '))
    contrib = date.today().year-aux['Contratação']
    if aux['Sexo'] == 'F':
        aux['AposentarContrib'] = int(30-contrib)
        aux['AposentarIdade'] = int(62-aux['Idade'])
        aux['AposentarPontos'] = int(93-aux['Idade']-contrib)
    if aux['Sexo'] == 'M':
        aux['AposentarContrib'] = int(35-contrib)
        aux['AposentarIdade'] = int(65-aux['Idade'])
        aux['AposentarPontos'] = int(103-aux['Idade']-contrib)
    aux['Salário'] = float(input('Salário: R$'))
cadastro = aux.copy()
del aux
print(f'\n{'-'*52}')
print(f'\n{cadastro['Nome']} com {cadastro['Idade']} anos e {contrib} de contribuição.\nVocê ainda precisa de {cadastro['AposentarContrib']} anos de contribuição\ne mais {cadastro['AposentarIdade']} anos de idade para aposentar.')
print(f'\nCaso faça a opção por se aposentar pela \nregra da pontuação, faltam {cadastro['AposentarPontos']} pontos.')
print(f'\nAposentando com o tempo mínimo de contribuição,\nterá o direito a receber R${cadastro['Salário']*0.6:.2f}.')
print(f'\n{' FIM DO PROGRAMA ':_^52}')