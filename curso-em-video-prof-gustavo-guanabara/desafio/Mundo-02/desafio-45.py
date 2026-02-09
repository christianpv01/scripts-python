'''Crie um programa que faça o computador jogar Jokenpô com você'''
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
from random import randint
from time import sleep
print('{} {}Desafio 45{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}JO-KEN-PÔ:{}\n'.format(cores['branco_s'],cores['limpa']))
print(' Escolha entre Pedra, Papel ou Tesoura.')
jokenpo = {1:'Pedra',
           2:'Papel',
           3:'Tesoura'
           }
computador = randint(1,3)
jogador = int(input(' 1. Pedra\n 2. Papel\n 3. Tesoura\n Escolha: '))
print('',flush=True)
sleep(2)
print(' JO',end='-',flush=True)
sleep(1)
print('KEN',end='-',flush=True)
sleep(1)
print('PÔ!!\n')
if jogador == 1 and computador == 3 or jogador == 2 and computador == 1 or jogador == 3 and computador == 2:
    print(' COMPUTADOR: {}.\n JOGADOR: {}.\n'.format(jokenpo[computador],jokenpo[jogador]))
    print(' {}PARABÉNS, VOCÊ VENCEU!!{}'.format(cores['verde_b'],cores['limpa']))
elif jogador == computador:
    print(' COMPUTADOR: {}.\n JOGADOR: {}.\n'.format(jokenpo[computador],jokenpo[jogador]))
    print(' {}EMPATOU!!{}'.format(cores['amarelo_b'],cores['limpa']))
else:
    print(' COMPUTADOR: {}.\n JOGADOR: {}.\n'.format(jokenpo[computador],jokenpo[jogador]))
    print(' {}VOCÊ PERDEU!!{}'.format(cores['vermelho_b'],cores['limpa']))
print('')