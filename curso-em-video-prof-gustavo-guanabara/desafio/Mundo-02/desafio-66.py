'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
    que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsidere a flag).'''

cores = {'limpa':'\033[m',
         'negativo':'\033[7m',
         'ciano_b':'\033[1;36m',
         'verde_b':'\033[1;32m',
         'vermelho_b':'\033[1;31m',
         'branco_fb':'\033[1;37;40m',
         'branco_s':'\033[4m',
         'amarelo_b':'\033[1;33m',
         'azul_b':'\033[1;34m',
         'roxo_b':'\033[1;35m'}
coresint = {1:'\033[1;36m',
            2:'\033[1;32m',
            3:'\033[1;31m',
            4:'\033[1;33m',
            5:'\033[1;34m',
            6:'\033[1;35m'}
from random import randint
#layout = '='*20                                                                          -- Modo antigo
#print('{} {}Desafio 66{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))     -- Modo antigo
#print(' {}Soma de inteiros usando break.{}\n'.format(cores['branco_s'],cores['limpa']))  -- Modo antigo
print(f'{'='*20} {cores["negativo"]}{'Desafio 66':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Soma de inteiros usando break.{cores['limpa']}\n')
print(' Caso queira parar, digite 999.')
núm = cont = soma = 0
while True:
    núm = int(input(' Digite um número: '))
    if núm == 999:
        break
    cont += 1
    soma += núm
print(f'\n Números informados: {coresint[randint(1,6)]}{cont}{cores["limpa"]}.\n Soma: {coresint[randint(1,6)]}{soma}{cores["limpa"]}.')