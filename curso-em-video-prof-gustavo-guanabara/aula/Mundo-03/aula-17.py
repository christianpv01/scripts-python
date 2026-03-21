'''Curso Python #17 - Listas (Parte 1)
    Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.


Tupla ()

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
               0          1        2        3
print(lanche[2])      <- Imprime pizza
lanche[3] = 'Picolé'  <- Não é possível, pois a tupla é IMUTÁVEL


Lista []

-> As listas são MUTÁVEIS!!

lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
indices        0          1        2        3

lanche[3] = 'Picolé'  <- Vai alterar o 'Pudim' para 'Picolé' 
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Picolé'] <- Nova lista

lanche.append('Biscoito')  <- Cria o elemento 4 e adiciona o 'Biscoito'
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Picolé','Biscoito'] <- Nova lista

lanche.insert(0,'Cachorro-Quente') <- Adiciona em qualquer lugar da lista
lanche = ['Cachorro-Quente', 'Hamburguer', 'Suco', 'Pizza', 'Picolé','Biscoito'] <- Nova lista

del lanche[3]              <- Serve para apagar a lista ou o valor do indice
lanche.pop(3)              <- Apaga o valor de indice utilizado, mas se não informar, remove os valores do final para o primeiro
lanche.remove('Pizza')     <- Precisa apontar o valor que você quer eliminar
lanche = ['Cachorro-Quente', 'Hamburguer', 'Suco', 'Picolé','Biscoito'] <- Nova lista

Se tentar remover um valor que não consta na lista, você vai receber um erro.
Para esses casos, a melhor forma é utilizar um If com in
if 'Pizza' in lanche:
    lanche.remove('Pizza')
Assim ele vai verificar antes se existe 'Pizza' dentro da lista para depois remover ou não.

valores = list(range(4, 11))    <- Cria uma lista ordenada
valores = [4, 5, 6, 7, 8, 9, 10]
indices    0  1  2  3  4  5  6

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()                  <- Ordena a lista em ordem crescente
valores.sort(reverse=True)      <- Ordena a lista em ordem decrescente

len(valores)                    <- Diz quantos elementos possui
'''

num = [2, 5, 9, 1]
print(num)
num[2] = 3                                                #<- Altera o número 9 para 3
print(num)
num.append(7)                                             #<- Adiciona o número 7 a lista  
print(num)
num.sort()                                                #<- Organiza a lista de forma crescente
print(num)
num.sort(reverse=True)                                    #<- Organiza a lista de forma decrescente
print(num)
print(f'Essa lista tem {len(num)} elementos.')            #<- Mostra a quantidade de elementos da lista
num.insert(2, 0)                                          #<- Adiciona o número 0 depois do segundo elemento
print(num)
num.pop()                                                 #<- Elimina o último número da lista que é o 1
print(num)
num.pop(2)                                                #<- Elimina o segundo elemento, começando do 0, então remove o 0
print(num)
num.insert(2, 2)                                          #<- Adiciona o número 2 depois do 2 elemento
print(num)
num.remove(2)                                             #<- Remove apenas o primeiro número do indice
print(num)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

val = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

a = [2, 3, 4, 7]
b = a                                                     #<- Cria uma ligação entre as variáveis, então qualquer alteração vai 
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')