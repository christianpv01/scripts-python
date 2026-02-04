#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro = Ana
#último = Souza
print('{0} Desafio 27 {0}'.format('='*10))
nome = input(' Informe o nome completo: ').strip().split()
print(' Primeiro nome: ',min(nome))
print(' Último nome:   ',max(nome))