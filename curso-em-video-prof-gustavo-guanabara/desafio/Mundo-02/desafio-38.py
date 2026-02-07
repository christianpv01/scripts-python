'''Escreva um programa que leia dois números inteiros e compare-os 
    mostrando na tela uma mensagem:
    O primeiro valor é maior
    O segundo valor é maior
    Não existe valor maior, os dois são iguais'''
layout = '='*20
cores = {'limpa':'\033[m',
         'negativo':'\033[7m',
         'ciano_b':'\033[1;36m',
         'verde_b':'\033[1;32m',
         'vermelho_b':'\033[1;31m',
         'branco_fb':'\033[1;37;40m',
         'branco_s':'\033[4m'
         }
print('{} {}Desafio 38{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Comparação de valores:{}\n'.format(cores['branco_s'],cores['limpa']))
n1 = int(input(' Digite o 1º valor: '))
n2 = int(input(' Digite o 2º valor: '))
if n1 > n2:
    print('\n O 1º número é {}MAIOR{} que o 2º.'.format(cores['ciano_b'],cores['limpa']))
elif n1 < n2:
    print('\n O 2º número é {}MAIOR{} que o 1º.'.format(cores['verde_b'],cores['limpa']))
else:
    print('\n {}VALORES IGUAIS!!{}'.format(cores['vermelho_b'],cores['limpa']))
print(' \n FIM DO PROGRAMA!!')