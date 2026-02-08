'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
    calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
    Abaixo de 18.5: Abaixo do peso
    18.5 até 25: Peso ideal
    25 até 30: Sobrepeso
    30 até 40: Obesidade
    40+: Obesidade mórbida'''
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
altura = float(input(' Altura(m): '))
peso = float(input(' Peso(kg): '))
imc = peso / (altura**2)
print('')
if imc < 18.5:
    print(' {}Classificação: Abaixo do peso ideal.\n Procure um médico para auxiliar.{}'.format(cores['vermelho_b'],cores['limpa']))
elif imc >= 18.5 and imc < 25:
    print(' {}Classificação: Peso ideal.\n Continue assim!!{}'.format(cores['verde_b'],cores['limpa']))
elif imc >= 25 and imc < 30:
    print(' {}Classificação: Sobrepeso.\n Vamos nos cuidar!!{}'.format(cores['amarelo_b'],cores['limpa']))
elif imc >= 30 and imc < 40:
    print(' {}Classificação: Obesidade.\n Procure um médico para auxiliar.{}'.format(cores['roxo_b'],cores['limpa']))
else:
    print(' {}Classificação: Obesidade mórbida.\n Por favor, procure um médico para auxiliar.{}'.format(cores['vermelho_b'],cores['limpa']))
print('')