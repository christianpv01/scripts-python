'''Refaça o Desafio 35 dos triângulos, acrescentando o recurso de 
    mostrar que tipo de triângulo será formado:
    Equilátero: todos os lados iguais
    Isósceles: dois lados iguais
    Escaleno: todos os lados diferentes'''
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
print('{} {}Desafio 42{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Tipos de triângulo:{}\n'.format(cores['branco_s'],cores['limpa']))
print(' Informe abaixo o valor de três segmentos de reta.')
l1 = float(input(' 1º Segmento: '))
l2 = float(input(' 2º Segmento: '))
l3 = float(input(' 3º Segmento: '))
if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('\n {}Com os segmentos informados, não formam um triângulo.{}\n'.format(cores['vermelho_b'],cores['limpa']))
else:
    if l1 == l2 and l1 == l3:
        print('\n Com os segmentos informados, formamos um triângulo {}EQUILÁTERO{}\n'.format(cores['ciano_b'],cores['limpa']))
    elif l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l2 != l1:
        print('\n Com os segmentos informados, formamos um triângulo {}ISÓSCELES{}\n'.format(cores['azul_b'],cores['limpa']))
    else:
        print('\n Com os segmentos informados, formamos um triângulo {}ESCALENO{}\n'.format(cores['roxo_b'],cores['limpa']))