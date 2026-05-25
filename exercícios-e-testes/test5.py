# %%
def par_impar(numero:int)->str:
    '''par_impar função para verificar se o número é par ou ímpar.

    numero:
        número inteiro para a verificação
    
    exibe na tela:
        se é par ou ímpar
    '''
    if numero % 2 == 0:
        print('O número é par!')
    else:
        print('O número é ímpar')

# %%

numero = input('Entre com um número: ')
numero = int(numero)
par_impar(numero)

# %%
def soma(valores:list)->float:
    return sum(valores)

def media(valores:list)->float:
    return soma(valores)/len(valores)

print('média: ', media([10,20,30,40,50]))
# %%
def soma(a:float, b:float, *args:float)->float:
    valores = [a,b]+ list(args)
    return sum(valores)

def media(a:float, b:float, *args:float)->float:
    return soma(a, b, *args) / (len(args)+2)

a = float(input('entre com o valor de a: '))
b = float(input('entre com o valor de b: '))
c = float(input('entre com o valor de c: '))

print('Média', media(a,b,c))