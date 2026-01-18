#Faça um programa que leia um número inteiro e
#mostre na tela o seu sucessor e seu antecessor.
print('{0} Desafio 05 {0}'.format('='*10))
num = int(input('Digite um número inteiro: '))
print('O número {} tem como antecessor o número {} e como sucessor o número {}.'.format(num, (num - 1), (num + 1 )))
print('='*32)