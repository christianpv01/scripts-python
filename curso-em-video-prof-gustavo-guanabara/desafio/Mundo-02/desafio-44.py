'''Elabore um programa que calcule o valor a ser pago por um produto,
    considerando o seu preço normal e condição de pagamento:
    À vista no dinheiro ou pix: 10% de desconto
    À vista no cartão de crédito: 5% de desconto
    2x no cartão: preço normal
    3x ou mais no cartão: 20% de juros'''
layout = '='*20
cores = {'limpa':'\033[m',
         'negativo':'\033[7m',
         'ciano_b':'\033[1;36m',
         'verde_b':'\033[1;32m',
         'vermelho_b':'\033[1;31m',
         'branco_fb':'\033[1;37;40m',
         'branco_s':'\033[4m',
         'amarelo_b':'\033[1;33m',
         'azul_b':'\033[1;34m',
         'roxo_b':'\033[1;35m'
         }
print('{} {}Desafio 44{} {}'.format(layout,cores['negativo'],cores['limpa'],layout))
print(' {}Calculadora de desconto sobre produto:{}\n'.format(cores['branco_s'],cores['limpa']))
print(' Informe abaixo o valor do produto e a forma de pagamento.')
produto = float(input(' Valor do produto: R$'))
forma_pag = int(input(' Forma de pagamento:\n 1. À vista em dinheiro ou pix\n 2. À vista no cartão de crédito\n 3. 2x no cartão de crédito\n 4. 3x ou mais no cartão de crédito\n '))
if forma_pag == 4:
    parcelas = int(input(' Número de parcelas: '))
if forma_pag == 1:
    print('\n Desconto de 10% aplicado.\n Valor do Produto atualizado: R${:.2f}.\n'.format(produto*.90))
elif forma_pag == 2:
    print('\n Desconto de 5% aplicado.\n Valor do Produto atualizado: R${:.2f}.\n'.format(produto*.95))
elif forma_pag == 3:
    print('\n Valor do Produto: R${:.2f}.\n Valor da parcela: 2x R${:.2f}.\n'.format(produto,produto/2))
elif forma_pag == 4:
    print('\n Juros de 20% aplicado.\n Valor final do Produto: R${:.2f}.\n Valor da parcela: {}x R${:.2f}.'.format(produto*1.20,parcelas,(produto*1.20)/parcelas))