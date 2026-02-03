'''Faça um programa que leia três números e mostre
    qual é o maior e qual é o menor.'''
print('{0} Desafio 33 {0}'.format('='*10))
print(' Maior e menor número')
n1 = int(input(' 1º número: '))
n2 = int(input(' 2º número: '))
n3 = int(input(' 3º número: '))
print(' O maior número foi: {}'.format(max(n1,n2,n3)))
print(' O menor número foi: {}'.format(min(n1,n2,n3)))