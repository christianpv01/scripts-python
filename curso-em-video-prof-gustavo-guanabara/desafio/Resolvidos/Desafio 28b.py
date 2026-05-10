from random import randint
from time import sleep
computador = randint(0,5) #Faz o sorteio entre 0 e 5
l1 = '-=-'*20
print(l1)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(l1)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('Processando..')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vener!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador,jogador))