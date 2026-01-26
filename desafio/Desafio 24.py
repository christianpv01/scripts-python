#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
print('{0} Desafio 24 {0}'.format('='*10))
cidade = input(' Digite o nome de uma cidade: ').strip()
cidade = cidade.title()
print(cidade[:5] == 'Santo')