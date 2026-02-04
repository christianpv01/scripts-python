'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
    Para salários superiores a R$1.250,00, calcule um aumento de 10%.
    Para os inferiores ou iguais, o aumento é de 15%.'''
print('{0} Desafio 34 {0}'.format('='*10))
print(' Aumento salarial de 10% até 15%')
salario = float(input(' Informe o salário: R$'))
if salario > 1250:
    print(' Seu salário teve um reajuste para: R${:.2f}'.format(salario*1.1))
else:
    print(' Seu salário teve um reajuste para: R${:.2f}'.format(salario*1.15))