#Faça um que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m².
print('{0} Desafio 11 {0}'.format('='*10))
print()
largura = float(input('Qual a largura da parede em metros? '))
print()
altura = float(input('Qual a altura da parede em metros? '))
m2 = largura * altura
print()
tinta = m2 / 2
print('Em {} m², vamos precisar de {} litros de tinta'.format(m2, tinta))