'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
    Faça também um programa que importe esse módulo e use algumas dessas funções.'''
'''Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.'''
'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
    informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108.'''
from pacotes import desafio107 as d107

núm = float(input('Digite um valor: R$ '))
print(f'O dobro de R$ {núm:.2f} é R$ {d107.dobro(núm):.2f}')
print(f'A metade de R$ {núm:.2f} é R$ {d107.metade(núm):.2f}')
print(f'Um juros de 15% sobre o valor de R$ {núm:.2f} fica no total de R$ {d107.aumentar(núm, 15):.2f}')
print(f'O desconto de 13% sobre o valor de R$ {núm:.2f} fica no total de R$ {d107.diminuir(núm, 13):.2f}')