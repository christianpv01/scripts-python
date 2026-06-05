# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas
# %%
# Utilizando for
soma_altura = 0
for i in range(4):
    altura = float(input(f'{i+1}ª altura: '))
    soma_altura += altura
print(f'O total das alturas somadas foi de {soma_altura:.2f}')

# %%
# Utilizando while
count = soma_altura = 0
while count < 4:
    altura = float(input(f'{count+1}ª altura: '))
    soma_altura += altura
    count += 1
print(f'O total das alturas somadas foi de {soma_altura:.2f}')
