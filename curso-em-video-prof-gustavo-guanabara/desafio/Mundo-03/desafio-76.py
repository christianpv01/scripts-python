'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
    No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 76':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Listagem de preços.{cores['limpa']}')
print()

Lista = ('Arroz',4.00,'Açúcar',2.50,'Café',28.70,'Feijão',7.35,'Leite',3.99,'Pão',0.60)
print(coresint[randint(1,5)])
print('-'*52)
print(f'{'LISTAGEM DE PREÇOS':^52}')
print('-'*52)

for c in range(0,len(Lista),2):
    print(f'{Lista[c]:.<40}{f'R$ {Lista[c+1]:7.2f}'}')

print('-'*52)
print(cores['limpa'])