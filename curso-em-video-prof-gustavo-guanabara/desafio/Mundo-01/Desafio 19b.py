from random import choice
print('{0} Desafio 19 {0}'.format('='*10))
print('')
nome1 = input('Qual o primeiro nome? ')
nome2 = input('Qual o segundo nome? ')
nome3 = input('Qual o terceiro nome? ')
nome4 = input('Qual o quarto nome? ')
lista = [nome1,nome2,nome3,nome4]
escolhido = choice(lista)
print('')
print(' Quem vai apagar o quadro? ')
print(f' Vai ser: {escolhido}')