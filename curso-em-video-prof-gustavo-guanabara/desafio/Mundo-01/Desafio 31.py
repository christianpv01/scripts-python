'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
    Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
    até 200 Km e R$0,45 para viagens mais longas'''
print('{0} Desafio 31 {0}'.format('='*10))
print(' Calculando o total valor do percurso')
Km = int(input(' Quantos quilômetros foram percorridos? '))
max200 = 0.50
min200 = 0.45
if Km <= 200:
    print(' Valor cheio de R${:.2f}'.format(Km*max200))
else:
    print(' Valor promocional de R${:.2f}'.format(Km*min200))
#print(' Valor cheio de R${:.2f}'.format(Km*max200) if Km <= 200 else ' Valor promocional de R${:.2f}'.format(Km*min200)) - Condicional Simplificada