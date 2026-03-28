'''Curso Python #19 - Dicionários
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.'''
'''
Tuplas = ()
Listas = []
Dicionários = {}
'''
'''
dados = dict() #ou dados = {}
dados = {'nome':'Pedro','idade':25}
print(dados['nome'])               #Imprime 'Pedro'
print(dados['idade'])              #Imprime 25
dados['sexo'] = 'M'                #Adiciona uma chave 'sexo' e o valor 'M'
print(dados['sexo'])               #Imprime 'M'
del dados['idade']                 #Deleta a chave e o valor
print(dados)
'''
'''
filme = {'titulo':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'
        }
print(filme.values())             #Imprime os valores  -> 'Star Wars', 1977, 'George Lucas'
print(filme.keys())               #Imprime as chaves   -> 'titulo', 'ano', 'diretor'
print(filme.items())              #Imprime os itens    -> ('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')
for k, v in filme.items():
    print(f'O {k} é {v}')         #Imprime a key(k) e o values(v) onde pega o filme.items()
'''
# As listas são identificadas por números(indices) e os dicionários podem ser identificados por textos e números
# Na hora de declarar o dicionário utiliza os {}, mas na hora de referenciar os elementos utiliza []
'''
locadora = [{'titulo':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'},
        {'titulo':'Avengers',
        'ano':2012,
        'diretor':'Joss Whedon'},
        {'titulo':'Matrix',
        'ano':1999,
        'diretor':'Wachowski'}]
print(locadora[0]['ano'])        #Imprime do indice 0 e da chave 'ano' que é 1977
print(locadora[2]['titulo'])     #Imprime do indice 2 e da chave 'titulo' que é 'Matrix'
'''
#Parte Prática
'''
pessoas = {'nome': 'Christian', 'sexo': 'M', 'idade': 35}
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')
#del pessoas['sexo']
#pessoas['nome'] = 'Gustavo'
#pessoas['peso'] = 98.5          #Não precisa dar append() igual nas Listas
for k, v in pessoas.items():     #Enquanto nas Tuplas e nas Listas utilizamos o enumerate(), nos dicionários, utilizamos o items, key, values
    print(f'{k} = {v}')
'''
'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['uf'], '-',brasil[1]['sigla'])
'''
'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())                             #Para copiar dentro de um dicionário, utiliza o .copy()
for e in brasil:
    for v in e.values():
        print(v, end='')
    print()
'''