'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
    Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from pacotes import desafio107 as d107

núm = float(input('Digite um valor: R$ '))
print(f'O dobro de R$ {núm:.2f} é R$ {d107.dobro(núm):.2f}')
print(f'A metade de R$ {núm:.2f} é R$ {d107.metade(núm):.2f}')
print(f'Um juros de 15% sobre o valor de R$ {núm:.2f} fica no total de R$ {d107.aumentar(núm, 15):.2f}')
print(f'O desconto de 13% sobre o valor de R$ {núm:.2f} fica no total de R$ {d107.diminuir(núm, 13):.2f}')