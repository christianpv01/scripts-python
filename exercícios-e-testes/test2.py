# %%
# Escreva um programa que crie um dicionário com nomes de frutas como chaves e seus respectivos preços como valores.
# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

frutas = {
    'Maçã':1.50,
    'Banana':2.75,
    'Uva':1.90,
    'Pera':1.25,
    'Laranja':0.65,
    'Limão':1.25,
    'Goiaba':2.15,
    'Abacaxi':3.2,
    'Jaca':5.8
    }


fruta = input('Qual fruta deseja verificar? ')
if fruta in frutas:
    print(f'O preço da {fruta} é de R$ {frutas[fruta]}')
else:
    print('Entre com um valor válido!')

    

    
# %%
