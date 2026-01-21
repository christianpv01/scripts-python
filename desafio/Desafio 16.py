#Crie um programa que leia um número Real qualquer pelo teclado e 
#mostre na tela a sua porção Inteiro.
print('{0} Desafio 16 {0}'.format('='*10))
import math
num = float(input('Digite um número decimal: '))
inteiro = math.trunc(num)
print('O número {} tem a parte Inteira {}.'.format(num, inteiro))
