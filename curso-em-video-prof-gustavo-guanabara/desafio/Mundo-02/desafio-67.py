'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
    O programa será interrompido quando o número solicitado for negativo.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 67':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Tabuada usando break.{cores['limpa']}\n')
print(' Se o número for negativo, interrompe.')
núm = 0
tabuada = 1
while True:
    núm = int(input(' Infomere o número: '))
    print()
    if núm < 0:
        break
    while tabuada <= 10:
        print(f' {coresint[randint(1,6)]}{tabuada:>4} x{núm:>4} ={núm * tabuada:>4}{cores["limpa"]}')
        tabuada += 1
    print('~' * 30)
    tabuada = 1
print(' FIM')