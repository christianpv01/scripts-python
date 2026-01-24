import math
print('{0} Desafio 17 {0}'.format('='*10))
print('')
print(' Vamos calcular a hipotenusa')
catetoOP = float(input(' Digite o valor do cateto oposto: '))
catetoAD = float(input(' Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(catetoOP,catetoAD)
print(' >>> O valor da hipotenusa é {:.2f}'.format(hipotenusa))
print('')