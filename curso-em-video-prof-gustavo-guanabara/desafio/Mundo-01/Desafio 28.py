'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''
print('{0} Desafio 28 {0}'.format('='*10))
print(' Adivinhe o número entre 0 e 5')
from random import randint
num = randint(0,5)
chute = int(input(' Qual é o seu palpite? '))
print(' O número sorteado foi {}'.format(num))
if num == chute:
    print(' Você acertou!!')
else:
    print(' Você errou!!')
#print(' Você acertou!!' if num == chute else ' Você errou!!') - Condição simplificada