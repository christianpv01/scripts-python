#Faça um programa que leia um número inteiro qualquer e 
#mostre na tela a sua tabuada.
print('{0} Desafio 09 {0}'.format('='*10))
print()
numero = int(input('Qual número você gostaria de visualizar a sua tabuada? '))
auxiliar = 1
produto = numero * auxiliar
while auxiliar <= 10 :
    print('{} x {:2} = {}'.format(numero, auxiliar, produto))
    auxiliar = auxiliar + 1
    produto = numero * auxiliar
