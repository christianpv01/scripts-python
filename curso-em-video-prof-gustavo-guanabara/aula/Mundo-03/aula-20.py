'''
Curso Python #20 - Funções (Parte 1)
Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. 
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. 
Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.
'''
'''
#INTRO
def mostraLinha():
    print('-' * 40)

mostraLinha()
print(f'{'SISTEMA DE ALUNOS':^40}')
mostraLinha()
mostraLinha()
print(f'{'CADASTRO DE FUNCIONÁRIOS':^40}')
mostraLinha()
mostraLinha()
print(f'{'ERRO DO SISTEMA':^40}')
mostraLinha()

def mensagem(msg):
    print('-' * 40)
    print(msg)
    print('-' * 40)

mensagem(f'{'SISTEMA DE ALUNOS':^40}')
'''
#PARTE PRATICA
'''
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)
'''
'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

#PROGRAMA PRINCIPAL
soma(4, 5)
soma(a=4, b=5)                       #Podendo explicitar os valores
soma(b=4, a=5)
soma(8, 9)
soma(2, 1)
'''
'''
def contador(*núm):
    for valor in núm:
        print(valor)
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
'''
'''
def soma(*valores):
    s=0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos {s}')

soma(5,2)
soma(2,9,4)
'''