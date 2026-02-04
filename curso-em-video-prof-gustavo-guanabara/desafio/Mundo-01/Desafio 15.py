#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o 
#carro custa R$60 por dia e R$0,15 por Km rodado.
print('{0} Desafio 15 {0}'.format('='*10))
dia = int(input(' Quantos dias você utilizou o carro? '))
aluguel = 60.00 * dia
km = round(float(input(' Quanto foi a quilometragem percorrida? ')),2)
rodado = 0.15 * km
print()
print(' O carro foi alugado por {} dias. Resultando em R${:.2f}'.format(dia, aluguel))
print(' Quilometragem percorrida: {} km. Resultando em R${:.2f}'.format(km, rodado))
print('-'*32)
print(' >>> Preço final: R${:.2f}'.format(aluguel + rodado))
print()
