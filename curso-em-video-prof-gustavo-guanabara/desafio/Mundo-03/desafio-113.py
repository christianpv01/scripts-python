'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
    Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

from utilidadesCeV import dado

a = dado.leiaInt('Digite um número inteiro: ')

b = dado.leiaFloat('Digite um número real: ')
print(f'O valor inteiro foi {a} e o real foi {b}')