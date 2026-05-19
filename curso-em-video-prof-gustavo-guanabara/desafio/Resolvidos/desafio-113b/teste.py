'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
    Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

from utilidadescev import dado

n1 = dado.leiaInt('Digite um Inteiro: ')
n2 = dado.leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')