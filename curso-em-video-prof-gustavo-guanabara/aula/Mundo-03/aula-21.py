#Curso Python #21 - Funções (Parte 2)
'''
    Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre >Interactive Help< em Python, 
    o uso de >docstrings< para documentar nossas funções, >argumentos opcionais< para dar mais dinamismo em funções Python, 
    >escopo de variáveis< e >retorno de resultados<.
'''
'''
#Interactive Help

#help()
#print(input.__doc__)

#docstrings

#def contador(i,f,p):
    
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    
    c=i
    while c <= f:
        print(f'{c}',end='..')
        c+=p
    print('FIM!')

#contador(2,10,2)
#help(contador)

#Parametros Opcionais

#def somar(a=0,b=0,c=0):
    
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    
    s = a+b+c
    print(f'A soma vale {s}')

#somar(3,2,5)
#somar(8,4)
#somar()
#somar(b=4,c=2)
#somar(c=3,a=2)

#Escopo de Variáveis
#ex1
def teste(b):
    global a              #Faz o parametro de fora assumir o valor de dentro da def
    a = 8
    b+=4
    c=2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

#Programa principal
a = 5
teste(a)
print(f'A fora vale {a}')

#ex2
def funcao():
    n1=4
    print(f'N1 dentro vale {n1}')

n1=2
funcao()
print(f'N1 fora vale {n1}')

#Retornando Valores
def somar(a=0,b=0,c=0):
    s=a+b+c
    return s

r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')

#Prátrica 1
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os result6ados são {f1}, {f2} e {f3}.')

#Prática 2
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
'''