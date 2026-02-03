'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
    se elas podem ou não formar um triângulo.'''
print('{0} Desafio 35 {0}'.format('='*10))
print(' Verificar se forma um triângulo')
r1 = float(input(' 1ª reta: '))
r2 = float(input(' 2ª reta: '))
r3 = float(input(' 3º reta: '))
if r1<(r2+r3) and r2<(r1+r3) and r3<(r1+r2):
    print(' Formam um Triângulo!')
else:
    print(' NÃO formam um Triângulo!')