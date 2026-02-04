#Faça um algoritmo que leia o salário de um funcionário e
#mostre seu novo salário, com 15% de aumento.
print('{0} Desafio 13 {0}'.format('='*10))
print()
salario = round(float(input('Qual o salário do funcionário? R$ ')),2)
print()
aumento15 = salario * (115/100)
print('O novo salário foi para {}'.format(round(aumento15,2)))