'''A confederação nacional de natação precisa de um programa que leia o ano de
    nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    Até 9 anos: MIRIM
    Até 14 anos: INFANTIL
    Até 19 anos: JUNIOR
    Até 20 anos: SÊNIOR
    Acima: MASTER'''
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
print('{} {}Desafio 40{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Classificador de categoria:{}\n'.format(cores['branco_s'],cores['limpa']))
anoATUAL = 2026
print(' Para verificarmos a sua classificação, informe')
anoNASC = int(input(' Em que ano você nasceu? '))
idade = anoATUAL-anoNASC
print('')
if idade <= 9:
    print(' Classificação: {}MIRIM{}\n'.format(cores['ciano_b'],cores['limpa']))
elif idade >= 10 and idade <= 14:
    print(' Classificação: {}INFANTIL{}\n'.format(cores['azul_b'],cores['limpa']))
elif idade >= 15 and idade <= 19:
    print(' Classificação: {}JUNIOR{}\n'.format(cores['roxo_b'],cores['limpa']))
elif idade == 20:
    print(' Classificação: {}SÊNIOR{}\n'.format(cores['verde_b'],cores['limpa']))
else:
    print(' Classificação: {}MASTER{}\n'.format(cores['amarelo_b'],cores['limpa']))