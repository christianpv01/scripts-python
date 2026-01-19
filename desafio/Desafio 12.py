#Faça um algoritmo que leia o preço de um produto e
#mostre seu novo preço, com 5% de desconto.
print('{0} Desafio 12 {0}'.format('='*10))
print()
produto = round(float(input('Qual o valor do produto? R$ ')),2)
desconto = round(produto * (95/100),2)
print()
print('O valor do produto com desconto de 5% ficou em {} reais.'.format(desconto))