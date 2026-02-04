'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''
print('{0} Desafio 32 {0}'.format('='*10))
print(' Verificação de ano BISSEXTO')
ano = int(input(' Digite o ano: '))
v1 = ano%4
v2 = ano%400
v3 = ano%100
if v1 == 0 and v3 != 0:
    print(' O ano {} é BISSEXTO!'.format(ano))
elif v1 == 0 and v2 == 0:
    print(' O ano {} é BISSEXTO!'.format(ano))
else:
    print(' Não é BISSEXTO!')