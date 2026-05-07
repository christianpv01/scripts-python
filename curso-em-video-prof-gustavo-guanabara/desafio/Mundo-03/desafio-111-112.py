'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
    Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e matenha tudo funcionando.'''
'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
    Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma
    validação de dados para aceitar apenas valores que sejam monetários.'''

from utilidadesCeV import dado,moeda

n = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(n, 25, 15)