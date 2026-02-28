'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
    se o usuário vai continuar. No final, mostre:
    A) Qual é o total gasto na compra.
    B) Quantos produtos custam mais de R$1000.
    C) Qual é o nome do produto mais barato.'''

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
from time import sleep
print(f'{'='*20} {cores["negativo"]}{'Desafio 70':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Lista de compras usando break.{cores['limpa']}')
cont = mais1000 = maior_valor = soma = 0
while True:
    nome_produto = str(input('\n Qual o nome do produto? '))
    valor_produto = float(input(' Qual o valor do produto? R$'))
    cont += 1
    soma += valor_produto
    if valor_produto > 1000:
        mais1000 += 1
    if valor_produto > maior_valor:
        maior_valor = valor_produto
    if cont == 1:
        menor_valor = valor_produto
        produto = str(nome_produto)
    if valor_produto < menor_valor:
        menor_valor = valor_produto
        produto = str(nome_produto)
    print('')
    print('~' * 52)
    verificador = str(input(' Deseja continuar? [S/N]\n Escolha: ')).strip().upper()[0]
    print('~' * 52)
    if verificador not in 'Ss':
        break
print('')
print(f'{'Resultado':^56}')
print(f'\n O total gasto foi de R$ {soma:.2f}\n Quantos produtos a cima dos mil reais? {mais1000}\n O produto mais barato: {produto}.\n')
print('=' * 52)