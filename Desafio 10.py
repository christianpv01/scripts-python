#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
#mostre quantos Dólares ela pode comprar.
print('{0} Desafio 10 {0}'.format('='*10))
print()
real = float(input('Quantos reais você tem? '))
cotDol = 5.37    #Cotação em 18/01/2026.
print()
print('Com {} reais, você pode comprar {} dólares'.format(round(real,2),round((real/cotDol),2)))
