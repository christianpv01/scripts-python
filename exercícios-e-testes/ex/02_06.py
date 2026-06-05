# Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista:
#   laranja, cerveja, miojo, carvão, picanha.

lista = ['laranja', 'cerveja', 'miojo', 'carvão', 'picanha']
item = input('Escolha um item para comprar: ').lower()


if item in lista:
    print(f'O item {item} está na lista.')

else:
    print('Escolha um item válido!')