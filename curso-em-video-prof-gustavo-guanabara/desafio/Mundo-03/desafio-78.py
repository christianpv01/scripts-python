'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
    No final, mostre qual foi o maior e o menor vlaor digitado e as suas respectivas posições na lista'''

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

print(f'{'='*20} {cores["negativo"]}{'Desafio 78':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Lista com 5 valores.{cores['limpa']}')
print()

valores = list()
for v in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    
print('-' * 52)
print(f'Lista: {valores}')
#Maior valor
print(f'\nO maior valor foi {max(valores)} ',end='')
if valores.count(max(valores)) == 1:
    print(f'na {valores.index(max(valores))+1}ª posição')
else:
    print('nas posições ', end='')
    for cmax, vmax in enumerate(valores):
        if vmax == max(valores):
            print(f'{cmax+1}ª', end=' ')
#Menor valor        
print(f'\nO menor valor foi {min(valores)} ', end='')
if valores.count(min(valores)) == 1:
    print(f'na {valores.index(min(valores))+1}ª posição')
else:
    print('nas posições ', end='')
    for cmin, vmin in enumerate(valores):
        if vmin == min(valores):
            print(f'{cmin+1}ª', end=' ')
print()
print('-' * 52)