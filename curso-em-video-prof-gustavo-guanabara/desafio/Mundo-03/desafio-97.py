'''
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma 
mensagem com tamanho adaptável.
Ex: escreva('Olá,Mundo!')
Saída: 
~~~~~~~~~~
Olá,Mundo!
~~~~~~~~~~
'''
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
from datetime import date
print(f'{'='*20} {cores["negativo"]}{'Desafio 97':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Função de texto.{cores['limpa']}\n')

def escreva(msg):
    print(f'{'~'*(len(msg)+4)}\n  {msg}\n{'~'*(len(msg)+4)}')


escreva('Olá, mundo!')
escreva('Meu nome é Christian')