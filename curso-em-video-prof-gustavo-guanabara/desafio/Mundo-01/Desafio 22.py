#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome
print('{0} Desafio 22 {0}'.format('='*10))
nome = input('Diga o seu nome completo: ')
print('Analisando seu nome..')
print('Nome em maiúsculo: ',nome.upper()) #Toda string em maiúsculo
print('Nome em minúsculo: ',nome.lower()) #Toda string em minúsculo
print('Seu nome possui {} letras.'.format(len(''.join(nome.split())))) #Quantidade de caractere sem considerar os espaços
nomeSplit = nome.split()
print('Primeiro nome: {} tem {} letras.'.format(nomeSplit[0],len(nomeSplit[0])))