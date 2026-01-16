print('====== DESAFIO 03 ======')
print('Informe dois valores')
v1 = int(input('1º Valor: '))
v2 = int(input('2º Valor: '))
soma = v1 + v2
print()
print('A soma entre os valores',v1,'+',v2,'=',soma)
print()
if v1>v2 :
    print('O primeiro valor é maior que o segundo')
else :
    print('O segundo número é maior que o primeiro')
print()
if soma%2==0 :
    print('O número da soma dos valores é PAR')
else :
    print('O número da soma dos valores é ÍMPAR')
