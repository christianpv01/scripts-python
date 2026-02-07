'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    O programa vai pergutar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então 
    o empréstimo será negado.'''
from time import sleep
layout = '='*20
cores = {'limpa':'\033[m',
         'amarela_lb':'\033[1;33m',
         'vermelha_lb':'\033[1;31m',
         'verde_fb':'\033[1;42m',
         'amarelo_ls':'\033[4;33m'
         }
print('{0} Desafio 36 {0}'.format(layout))
print(' {}Empréstimo bancário{}'.format(cores['amarela_lb'],cores['limpa']))
valorCASA = float(input(' Qual é o valor do imóvel? R$'))
salário = float(input(' Informe seu salário: R$'))
parcela = int(input(' Em quantos anos quer financiar? '))
parcela = parcela * 12
prestação = valorCASA/parcela
print(' Analisando...')
sleep(2)
if prestação > salário*0.3:
    print(' Emprestimo: {}NEGADO!!{}'.format(cores['vermelha_lb'],cores['limpa']))
else:
    print(' Emprestimo: {}ACEITO!!{}'.format(cores['verde_fb'],cores['limpa']))
    sleep(1)
    print(' PARABÉNS PELA CONQUISTA!')
    sleep(1)
    print(' {}Sua parcela vai ficar no valor de R${:.2f}{}'.format(cores['amarelo_ls'],prestação,cores['limpa']))