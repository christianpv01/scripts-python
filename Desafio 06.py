#Crie um algoritmo que leia um número e
#mostre o seu dobro, triplo e raiz quadrada.
print('{0} Desafio 06 {0}'.format('='*10))
num = input('Digite um número: ')
print('O dobro de {} é {}'.format(num, int(num) * 2))
print('O triplo de {} é {}'.format(num, int(num) * 3))
print('A raiz quadrada de {} é {:.2f}'.format(num, float(num) ** (1/2)))
