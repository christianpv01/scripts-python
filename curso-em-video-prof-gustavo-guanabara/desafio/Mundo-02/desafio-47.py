'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50'''
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
print('{} {}Desafio 47{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Números pares entre 1 a 50{}\n'.format(cores['branco_s'],cores['limpa']))
print('\n {}Modelo 1{}'.format(cores['ciano_b'],cores['limpa']))
for c in range(0,51,2): #Modo simples
    print(c, end=' ')
print('')
print('\n {}Modelo 2{}'.format(cores['azul_b'],cores['limpa']))
for c in range(0,51):
    if c % 2 == 0:
        print(c, end=' ')
print('\n')