#Estruturas de repetição
'''Laço de repetição
        Parte 1'''

''' 1º
for c in range(1,10):
    passo
pega'''

''' 2º
for c in range(0,3):
    passo
    pula
passo
pega'''

'''3º
for c in range(0,3):
    if moeda:
        pega
    passo
    pula
passo
pega'''

for c in range(0, 5): #Exclui o último número
    print(c)
print('Fim')

for c in range(1, 6): #Exclui o último número
    print(c)
print('Fim')

for c in range(6, 0, -1): #Exclui o último número e precisa preencher o passo negativo
    print(c)
print('Fim')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))