'''Aula 16 - Tuplas'''

#() -> Tupla - As tuplas são IMUTÁVEIS, no Python não precisa do parenteses.
#[] -> Lista - As listas são MUTÁVEIS
#{} -> Dicionário

'''Parte prática'''

lanche = ('Hamburguer','Suco','Pizza','Pudim')
print(lanche[2]) #Imprime somente a terceira string dentro da variável composta
print(lanche[0:2]) #Imprime por fatiamento excluindo a última, eliminando a Pizza nesse exemplo
print(lanche[1:]) #Imprime todos os itens depois da segunda
print(lanche[:2]) #Imprime todos do inicio até o número final menos um
print(lanche[-1]) #Imprime o último elemento, número negativo corre a variável composta de trás para frente
print(lanche[-2:]) #Imprime o penúltimo elemento e depois a sequência dentro da tupla

print(len(lanche)) #Imprime a quantidades de elementos dentro da variável

for c in lanche: #Percorre a váriavel inteira
    print(c)

print('-'*40)
lanche = ('Hamburguer','Suco','Pizza','Pudim','Batata Frita')

for cont in range(0, len(lanche)): #For com range
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:              #For com a variavel
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche): #For com enumerate
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')
print('-'*40)
print(sorted(lanche)) #Ordena a tupla sem muda a variavel
print('-'*40)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b          #A soma das tuplas, apenas imprime os componentes, sem calcular
print(c)
print(len(c))      #mostra o tamanho da tupla
print(c.count(5))  #conta a quantidade de vezes que o 5 aparece
print(c.index(8))  #mostra a posição do número 8, lembrando que a contagem começa de 0, apenas a primeira ocorrência
print('-'*40)

pessoa = ('Christian', 36, 'M', 105)
del(pessoa)        #apaga a tupla inteira, não consegue apagar um item da tupla, pois ela é imutável
#print(pessoa)
