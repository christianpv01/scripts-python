#Faça um programa que leia um ângulo qualquer e mostre
#na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
print('{0} Desafio 18 {0}'.format('='*10))
print('  Calculadora de seno, cosseno e tangente')
print('-'*20)
angulo = int(input(' Informe o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(' Seno: {:.2f}\n Cosseno: {:.2f}\n Tangente: {:.2f}'.format(seno,cosseno,tangente))