#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex: Digite um número: 1834 - unidade: 4 - dezena: 3 - centena: 8 - milhar: 1
print('{0} Desafio 23 {0}'.format('='*10))
número = input(' Digite um número de 0 a 9999: ')
if len(número) == 1:
    unidade = número[0]
    dezena = 0
    centena = 0
    milhar = 0
elif len(número) == 2:
    unidade = número[1]
    dezena = número[0]
    centena = 0
    milhar = 0  
elif len(número) == 3:
    unidade = número[2]
    dezena = número[1]
    centena = número[0]
    milhar = 0
elif len(número) == 4:
    unidade = número[3]
    dezena = número[2]
    centena = número[1]
    milhar = número[0]
print('Milhar:  {}\nCentena: {}\nDezena:  {}\nUnidade: {}'.format(milhar,centena,dezena,unidade))