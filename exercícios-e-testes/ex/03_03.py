# Faça um programa que receba uma quantidade indefinida de valores
# correspondentes a "saldo em conta", mas quando o usuário apertar
# "enter" sem digitar valor algum, o programa para de receber valores,
# e exibe a soma de todos os valores digitados anteriormente.

# %%
saldo_conta = 0
while True:
    recebido = input('Digite o valor recebido: R$ ').replace(',','.')
    if recebido == '':
        break
    try:
        recebido = float(recebido)
    except Exception as err:
        print('Digite um valor válido!')
    else:
        saldo_conta += recebido

print(f'Saldo na conta: R$ {str(saldo_conta).replace('.',',')}')
