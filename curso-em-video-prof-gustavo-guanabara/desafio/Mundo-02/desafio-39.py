'''Faça um programa que leia o ano de nascimento de um jovem e informe,
    de acordo com sua idade:
    Se ele ainda vai se alistar ao serviço militar.
    Se é a hora de se alistar.
    Se já passou do tempo do alistamento.
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''
layout = '='*20
cores = {'limpa':'\033[m',
         'negativo':'\033[7m',
         'ciano_b':'\033[1;36m',
         'verde_b':'\033[1;32m',
         'vermelho_b':'\033[1;31m',
         'branco_fb':'\033[1;37;40m',
         'branco_s':'\033[4m'
         }
print('{} {}Desafio 39{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Alistamento Militar:{}\n'.format(cores['branco_s'],cores['limpa']))
anoATUAL = int(input(' Confirme em que ano estamos: '))
anoNASC = int(input(' Em qual ano nasceu? '))
idade = anoATUAL - anoNASC
verificação = abs(idade-18)
if idade < 18:
    if verificação > 1:
        print('\n {}Se prepare que faltam {} anos para o alistamento!{}'.format(cores['branco_s'],verificação,cores['limpa']))
    else:
        print('\n {}Se prepare que falta {} ano para o alistamento!{}'.format(cores['branco_s'],verificação,cores['limpa']))
elif idade == 18:
    print('\n {}Você está {}APTO{}{} para o Alistamento Militar{}'.format(cores['branco_s'],cores['verde_b'],cores['limpa'],cores['branco_s'],cores['limpa']))
else:
    print('\n Favor encaminhar-se até o quartel mais próximo!!!\n Seu tempo para alistamento passou em {} anos.'.format(verificação))
    print(' {}Você vai precisar pagar uma multa de R$6,38.{}'.format(cores['vermelho_b'],cores['limpa']))