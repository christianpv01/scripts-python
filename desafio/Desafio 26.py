#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
print('{0} Desafio 26 {0}'.format('='*10))
frase = str(input(' Digite uma frase qualquer: ')).strip().upper()
print(' A Letra "A" aparece {}x'.format(frase.count('A')))
print(' A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print(' A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))