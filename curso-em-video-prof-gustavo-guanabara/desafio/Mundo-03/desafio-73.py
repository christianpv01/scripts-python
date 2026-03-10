'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
    Depois mostre:
    A) Apenas os 5 primeiros colocados.
    B) Os últimos 4 colocados da tabela.
    C) Uma lista com os times em ordem alfabética.
    D) Em que posição na tabela está o time da Chapecoense.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 73':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Tabela do Brasileirão 2026.{cores['limpa']}')
print()

#A) Apenas os 5 primeiros colocados.
times = ('Palmeiras','São Paulo','Corinthians','Bahia','Fluminense','Athletico-PR','Bragantino','Grêmio','Chapecoense','Mirassol','Flamengo','Coritiba','Santos','Botafogo','Vitória','Remo','Atlético-MG','Internacional','Cruzeiro','Vasco')
print(f' {cores["verde_b"]}Os primeiros 5 colocados são:')
for top5 in range(0,5):
    sleep(0.2)
    print(f'  {top5+1}. {times[top5]}')
print(f'{cores["limpa"]}{'-'*52}')

#B) Os últimos 4 colocados da tabela.
times = ('Palmeiras','São Paulo','Corinthians','Bahia','Fluminense','Athletico-PR','Bragantino','Grêmio','Chapecoense','Mirassol','Flamengo','Coritiba','Santos','Botafogo','Vitória','Remo','Atlético-MG','Internacional','Cruzeiro','Vasco')
aux = 20
print(f' {cores["vermelho_b"]}Na zona de rebaixamento, os 4 últimos são:')
for reb4 in range(-1,3,1):
    sleep(0.2)
    print(f'  {aux}. {times[reb4]}')
    aux -= 1
print(f'{cores["limpa"]}{'-'*52}')

#C) Uma lista com os times em ordem alfabética.
times = ('Palmeiras','São Paulo','Corinthians','Bahia','Fluminense','Athletico-PR','Bragantino','Grêmio','Chapecoense','Mirassol','Flamengo','Coritiba','Santos','Botafogo','Vitória','Remo','Atlético-MG','Internacional','Cruzeiro','Vasco')
count = 0
times = sorted(times)
print(f' {cores["ciano_b"]}Times em ordem alfabética:')
while count <= 19:
    c = 1
    while c <= 4:
        sleep(0.1)
        print(f'  {count+1:>2}. {times[count]:<13}',end='')
        count += 1
        c += 1
    print()
print(f'{cores["limpa"]}{'-'*52}')

#D) Em que posição na tabela está o time da Chapecoense.
times = ('Palmeiras','São Paulo','Corinthians','Bahia','Fluminense','Athletico-PR','Bragantino','Grêmio','Chapecoense','Mirassol','Flamengo','Coritiba','Santos','Botafogo','Vitória','Remo','Atlético-MG','Internacional','Cruzeiro','Vasco')
print(f'{cores["amarelo_b"]} O time da Chapecoense está em {times.index('Chapecoense')+1}º lugar no Brasileirão 2026.')
print(f'{cores["limpa"]}{'-'*52}')

#Extra Exercício
times = ('Palmeiras','São Paulo','Corinthians','Bahia','Fluminense','Athletico-PR','Bragantino','Grêmio','Chapecoense','Mirassol','Flamengo','Coritiba','Santos','Botafogo','Vitória','Remo','Atlético-MG','Internacional','Cruzeiro','Vasco')
time = str(input(f' {cores["roxo_b"]}Para qual time você torce? '))
while time not in times:
    print(' Time inválido, tente novamente.')
    time = str(input(f' Digite novamente um time: '))
print(f' O seu time está na {times.index(time)+1}ª posição na tabela do Brasileirão 2026.')
if times.index(time) < 4:
    print(f' E o {time} está no G-4 e classificado para ingressar na Copa Libertadores da América.')
elif times.index(time) > 15:
    print(f' Infelizmente o {time} está na zona de rebaixamento.')
print(f'{cores["limpa"]}{'-'*52}')