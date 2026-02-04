#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" dentro do nome.
print('{0} Desafio 25 {0}'.format('='*10))
nome = input(' Diga seu nome completo: ').strip()
nome = nome.title()
if 'Silva' in nome:
    print('O nome possui Silva dentro dele.')
else:
    print('O nome não possui Silva dentro dele.')