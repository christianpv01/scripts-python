'''Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada Km aima do limite.'''
print('{0} Desafio 29 {0}'.format('='*10))
print(' Radar de velocidade')
velocidade = int(input(' Qual a velocidade que você passou? '))
val_multa = 7
if velocidade > 80:
    multa = (velocidade-80)*val_multa
    print(' Você foi multado em R${:.2f}'.format(multa))
else:
    print(' Muito bem, você está dentro da velocidade da via!')