# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

# %%
def escolha_agua():
    while True:
        type = int(input(' (1) Água mineral natural\n (2) Água mineral com gás\nEscolha um tipo de água: '))
        qtd = int(input('Quantas garrafas você quer? '))
        if type == 1:
            valor = 1.5 * qtd
            print('Valor total: R$',valor)
            break
        elif type == 2:
            valor = 2.5
            print('Valor total: R$',valor)
            break
        else:
            print('Entre com um valor válido!')
            continue
# %%

escolha_agua()