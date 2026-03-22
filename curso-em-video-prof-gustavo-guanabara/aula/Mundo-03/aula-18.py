'''Curso Python #18 - Listas (Parte 2)
    Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. 
    As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.'''
'''Recapitulação

dados = list()
dados.append('Christian')      <- Indice 0
dados.append(35)               <- Indice 1
print(dados[0])                <- 'Christian'
print(dados[1])                <- 25

pessoas = list()
pessoas.append(dados[:])       <- Por conta do fatiamento [:], cria uma cópia e não um espelho, caso não coloque o fatiamento
'''
'''Lista Composta
pessoas = [['Pedro',25], ['Maria',19], ['João',32]]  <- Lista composta
print(pessoas[0][0])                                 <- Pega o primeiro índice da lista pessoas e depois pega o primeiro indice da lista dados
print(pessoas[1][1])                                 <- Vai printar 19
print(pessoas[2][0])                                 <- Vai printar 'João'
print(pessoas[1])                                    <- Vai printar a lista toda ['Maria',19]

'''
'''#1
teste = list()
teste.append('Christian')
teste.append(35)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''
'''#2
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)                                                 #Printa a lista composta toda
print(galera[0])                                              #Printa a primeira lista dentro de galera
print(galera[0][0])                                           #Printa o primeiro indice de galera e primeiro indice da primeira lista 'João'
print(galera[2][1])                                           #Printa o primeiro indice da terceira lista '13'
for p in galera:
    print(p)                                                  #Printa cada lista
    print(p[0])                                               #Printa somente os nomes 
    print(p[1])                                               #Printa as idades
    print(f'{p[0]} tem {p[1]} anos de idade.')                #Printa o nome e idade, formatada
    '''
'''#3
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')'''