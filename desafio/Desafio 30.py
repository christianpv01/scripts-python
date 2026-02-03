'''Crie um programa que leia um número inteiro e mostre na 
    tela se ele é PAR ou ÍMPAR.'''
print('{0} Desafio 30 {0}'.format('='*10))
print(' Identificador de número Par ou Ímpar')
num = int(input(' Digite um número: '))
if num%2 == 0:
    print('O número {} é PAR'.format(num))
else:
    print(' O número {} é ÍMPAR'.format(num))
#print('O número {} é PAR'.format(num) if num%2 == 0 else ' O número {} é ÍMPAR'.format(num)) - Condição Simplificada