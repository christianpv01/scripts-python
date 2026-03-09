'''Crie um programa que tenha uma tupla totalemnte preenchida com uma contagem por extenso, de 0 até 20
    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso'''

cores = {'limpa':'\033[m',                          #Dicionário de cores por string
         'negativo':'\033[7m',
         'ciano_b':'\033[1;36m',
         'verde_b':'\033[1;32m',
         'vermelho_b':'\033[1;31m',
         'branco_fb':'\033[1;37;40m',
         'branco_s':'\033[4m',
         'amarelo_b':'\033[1;33m',
         'azul_b':'\033[1;34m',
         'roxo_b':'\033[1;35m'}
coresint = {1:'\033[1;36m',                         #Dicionário de cores por inteiro
            2:'\033[1;32m',
            3:'\033[1;31m',
            4:'\033[1;33m',
            5:'\033[1;34m',
            6:'\033[1;35m'}
from random import randint
from time import sleep
print(f'{'='*20} {cores["negativo"]}{'Desafio 72':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Número por extenso de 0 a 20.{cores['limpa']}')

ext = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

núm = int(input('\n Número entre 0 e 20\n Escolha: '))
print(f' O número {núm} escrito por extenso -> {coresint[randint(1,6)]}{ext[núm].capitalize()}{cores["limpa"]}')