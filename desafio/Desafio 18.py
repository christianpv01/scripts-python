#Faça um programa que leia um ângulo qualquer e mostre
#na tela o valor do seno, cosseno e tangente desse ângulo.
import math
print('{0} Desafio 18 {0}'.format('='*10))
print('-'*20)
print('  Calculadora de seno, cosseno e tangente')
angulo = int(input(' Informe o ângulo: ')) 
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('O ângulo de: {}º\n Seno: {}\n Cosseno: {}\n Tangente: {}'.format(angulo,seno,cosseno,tangente))