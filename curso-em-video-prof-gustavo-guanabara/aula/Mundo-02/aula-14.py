#Estrutura de repetição while
'''Utiliza quando não possui um valor definido de range, colocando uma condicional para o término da repetição
    Ex: Enquanto c <= 10 faça c += 1, então vai repetir até chegar no 10 e sair da repetição.'''
c = 1
while c <= 10:
    print(c, end=' ')
    c += 1
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))