'''Crie um programa que tenha um tupla com várias palavras(não usar acentos).
    Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

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
print(f'{'='*20} {cores["negativo"]}{'Desafio 77':^}{cores["limpa"]} {'='*20}')
print(f' {cores['branco_s']}Quais são as vogais.{cores['limpa']}')
print()

Palavras = ('Paralelepipedo','Maionese','CD','Lanterna','Arara','Carro','Motocicleta','DVD','Musical')

a = e = i = o = u = somavogal = 0

Escolha = int(input('Escolha a palavra para verificação\n [1] Paralelepipedo\n [2] Maionese\n [3] CD\n [4] Lanterna\n [5] Arara\n [6] Carro\n [7] Motocicleta\n [8] DVD\n [9] Musical\n Escolha: '))
Escolha -= 1

a = Palavras[Escolha].upper().count('A')
e = Palavras[Escolha].upper().count('E')
i = Palavras[Escolha].upper().count('I')
o = Palavras[Escolha].upper().count('O')
u = Palavras[Escolha].upper().count('U')
somavogal = a + e + i + o + u
print('-'*52)
if somavogal > 0:
    print(f' A palavra {Palavras[Escolha]} possui {somavogal} vogais.')
else:
    print(f' A palavra {Palavras[Escolha]} não possui vogais.')
if a != 0:
    print(f' Tendo {a} letra(s) A.')
if e != 0:
    print(f' Tendo {e} letra(s) E.')
if i != 0:
    print(f' Tendo {i} letra(s) I.')
if o != 0:    
    print(f' Tendo {o} letra(s) O.')
if u != 0:
    print(f' Tendo {u} letra(s) U.')
print('-'*52)