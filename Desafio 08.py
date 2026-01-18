#Escreva um programa que leia um valor em metros e o exiba convertido 
#em centímetros e milímetros.
print('{0} Desafio 08 {0}'.format('='*10))
print()
m = int(input('Digite um valor em metros: '))
cm = m * 100
mm = m * 1000
print()
print('O valor de {} metros, representa {} centímetros e {} milímetros'.format(m, cm, mm))