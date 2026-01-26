#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
print('{0} Desafio 24 {0}'.format('='*10))
cidade = input(' Digite o nome de uma cidade: ')
cidade = cidade.title()
if 'Santo' in cidade:
    print('A cidade começa com Santo.')
else:
    print('A cidade não começa com Santo.')