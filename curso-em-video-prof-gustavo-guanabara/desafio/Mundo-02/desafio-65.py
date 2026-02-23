'''Crie um programa que leia vários números inteiro pelo teclado.
    No final da execução, mostre a média entre todos os vlaores e
    qual foi o maior e o menos valores lidos. o programa deve perguntar
    ao usuário se ele quer ou não continuar a digitar valores.'''
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
print('{} {}Desafio 65{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Média de inteiros, maior e menor.{}\n'.format(cores['branco_s'],cores['limpa']))
média = 0
soma = 0
contagem = 0
maior = 0
menor = 99999
verificador = 1
while verificador == 1:
    número = int(input(f' {cores["amarelo_b"]}Digite um número: '))
    contagem += 1
    soma += número
    if número > maior:
        maior = número
    elif número < menor:
        menor = número
    verificador = int(input(f'\n{cores["limpa"]} Deseja continuar?\n {cores["verde_b"]}[1] Sim\n {cores["vermelho_b"]}[2] Não\n {cores["limpa"]}Escolha: '))
média = float(soma / contagem)

print(f'\n{coresint[randint(1,6)]} A média dos valores foi de {média:.2f}.\n O maior número foi {maior} e o menor foi {menor}.{cores['limpa']}')