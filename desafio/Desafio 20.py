#O mesmo professor do desafio anterior quer sortear a ordem de apresentação
#de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
#e mostre a ordem sorteada.
from random import shuffle
print('{0} Desafio 20 {0}'.format('='*10))
print('')
nome1 = input('Qual o nome do 1º aluno? ')
nome2 = input('Qual o nome do 2º aluno? ')
nome3 = input('Qual o nome do 3º aluno? ')
nome4 = input('Qual o nome do 4º aluno? ')
lista = [nome1,nome2,nome3,nome4]
fila = shuffle(lista)
print('A ordem da apresentação será\n',lista)