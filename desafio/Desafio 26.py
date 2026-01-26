#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
print('{0} Desafio 26 {0}'.format('='*10))
frase = input(' Digite uma frase qualquer: ')
fraseUPPER = frase.upper()
print('A Letra "A" aparece {}x'.format(fraseUPPER.count('A')))
print(fraseUPPER.split(str(fraseUPPER.count('A'))))
#print('Aparecendo a primeira vez na posição {}'.format(min(fraseUPPER.find('A'))))