'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''
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
coresint = {
         1:'\033[1;36m',
         2:'\033[1;32m',
         3:'\033[1;31m',
         4:'\033[1;33m',
         5:'\033[1;34m',
         6:'\033[1;35m'
         }
from random import randint
print('{} {}Desafio 62{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Progressão Aritmética 2.{}\n'.format(cores['branco_s'],cores['limpa']))
termo1 = int(input(' 1º Termo: '))
razão = int(input(' Razão: '))
termos = int(input(' Quantidade de termos: '))
verificação = 0
print('')
while termos != 0:
    
    print(' {}{}{}'.format(coresint[randint(1,6)],termo1,cores['limpa']), end=' ')
    termo1 += razão
    verificação += 1
    if verificação == termos:
        print('')
        verificação = int(input('\n [1] Continuar\n [0] Sair\n Escolha: '))
        if verificação == 1:
            termos = int(input(' Mais quantos termos: '))
            termos += 1
            print('')
        else:
            termos = 0
            
print('\n {0} FIM {0}'.format(('-'*10)))