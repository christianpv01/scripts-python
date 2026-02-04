#Faça um programa que leia o comprimento do cateto oposto e
#do cateto adjacente de um triângulo retângulo, calcule e
#mostre o comprimento da hipotenusa
from math import sqrt
print('{0} Desafio 17 {0}'.format('='*10))
print(' Calculando o valor da hipotenusa de um triangulo retangulo')
print('-'*20)
c1 = int(input(' Digite o valor do cateto oposto: '))
c2 = int(input(' Digite o valor do cateto adjacente: '))
hip = sqrt(c1**2 + c2**2)  #Fórmula da hipotenusa -> h² = c1² + c2² -> h = raiz_quadrada(c1² + c2²)
print('-'*20)
print('O valor da hipotenusa é {}'.format(round(hip,2)))
