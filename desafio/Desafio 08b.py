#Escreva um programa que leia um valor em
#metros e o exiba convertido em km, hm, dam, dm, cm, mm
print('{0} Desafio 08b {0}'.format('='*10))
print()
metro = float(input('Digite o valor em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print('{} km.\n{} hm.\n{} dam.\n{:.0f} m.\n{:.0f} dm.\n{:.0f} cm.\n{:.0f} mm.'.format(km, hm, dam, metro, dm, cm, mm))
