'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
        'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
        'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
verificação = 'S'
while True:
        while True:
                núm = int(input('Digite um número entre 0 e 20: '))
                if 0 <= núm <= 20:
                        break
                print('Tente novamente. ', end='')
        print(f'Você digitou o número {cont[núm]}')
        print('-'*52)
        verificação = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if verificação != 'S':
                break
print('-'*52)