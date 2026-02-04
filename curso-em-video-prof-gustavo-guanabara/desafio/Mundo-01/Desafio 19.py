#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
print('{0} Desafio 19 {0}'.format('='*10))
print(' Sorteador de quem apagara o quadro')
aluno = random.randint(1,4)
print('>>> Hoje vai ser ',end='')
if aluno == 1:
    print('o Claudio')
if aluno == 2:
    print('a Ana')
if aluno == 3:
    print('o Chris')
if aluno == 4:
    print('a Bia')