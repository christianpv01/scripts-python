'''
Curso Python #22 - Módulos e Pacotes
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python e reutilizar nossos códigos em outros projetos. 
Vamos aprender também como agrupar vários módulos em um pacote, ampliando ainda mais a modularização em grandes projetos em Python.
'''
'''
Modularização
> Surgiu no início da década de 60
> Sistemas ficando cada vez maiores
> Foco: dividir um programa grande
> Foco: aumentar a legibilidade
> foco> facilitar a manutenção
'''
from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O dobro de {num} é {numeros.triplo(num)}')
'''
Vantagens
> Organização do código
> Facilidade na manutenção
> Ocultação de código detalhado
> Reutilização em outros projetos
'''
'''
Pacotes - em outras linguagens chamam de Bibliotecas
'''