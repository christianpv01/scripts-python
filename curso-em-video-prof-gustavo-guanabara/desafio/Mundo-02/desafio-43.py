'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e
    mostre seu status, de acordo com a tabela abaixo:
    Abaixo de 18.5: Abaixo do peso
    entre 18.5 e 25: Peso ideal
    25 até 30: Sobrepeso
    30 até 40: Obesidade
    acima de 40: Obesidade mórbida'''
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
print('{} {}Desafio 43{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Calculadora de IMC:{}\n'.format(cores['branco_s'],cores['limpa']))
print(' Informe abaixo o seu peso e altura.')