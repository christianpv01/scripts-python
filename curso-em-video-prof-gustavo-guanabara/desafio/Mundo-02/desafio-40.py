'''Crie um programa que leia duas notas de um aluno e calcule a sua média,
    mostrando uma mensagem no final, de acordo com a média atingida:
    Média abaixo de 5.0: REPROVADO
    Média entre 5.0 e 6.9: RECUPERAÇÃO
    Média 7.0 ou superior: APROVADO'''
layout = '='*20
cores = {'limpa':'\033[m',
         'negativo':'\033[7m',
         'ciano_b':'\033[1;36m',
         'verde_b':'\033[1;32m',
         'vermelho_b':'\033[1;31m',
         'branco_fb':'\033[1;37;40m',
         'branco_s':'\033[4m',
         'amarelo_b':'\033[1;33m'
         }
print('{} {}Desafio 40{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Boletim:{}\n'.format(cores['branco_s'],cores['limpa']))
n1 = float(input(' 1ª Nota: '))
n2 = float(input(' 2ª Nota: '))
média = (n1+n2)/2
if média >= 7:
    print('\n Situação: {}APROVADO!{}\n MEUS PARABÉNS!!'.format(cores['verde_b'],cores['limpa']))
elif média < 7 and média >= 5:
    print('\n Situação: {}RECUPERAÇÃO!{}\n MELHOR ESTUDAR!!'.format(cores['amarelo_b'],cores['limpa']))
else:
    print('\n Situação: {}REPROVADO!{}'.format(cores['vermelho_b'],cores['limpa']))