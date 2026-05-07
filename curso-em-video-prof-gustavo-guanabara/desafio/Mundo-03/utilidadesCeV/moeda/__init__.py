def aumentar(n, p):
    n = round((n + ( n * ( p / 100 ))),2)
    return str(n).replace('.',',')

def diminuir(n, p):
    n = round((n - ( n * ( p / 100 ))),2)
    return str(n).replace('.',',')

def dobro(n):
    n = round((n * 2),2)
    return str(n).replace('.',',')

def metade(n):
    n = round((n / 2),2)
    return str(n).replace('.',',')

def resumo(n, a, d):
    
    print(f'{'-'*40}\n{'RESUMO DO VALOR':^40}\n{'-'*40}')
    print(f'{'Preço analisado':<16}:   R$ {str(n).replace('.',',')}')
    print(f'{'Dobro do preço':<16}:   R$ {dobro(n)}')
    print(f'{'Metade do preço':<16}:   R$ {metade(n)}')
    print(f'{f'{a}% de aumento':<16}:   R$ {aumentar(n, a)}')
    print(f'{f'{d}% de redução':<16}:   R$ {diminuir(n, d)}')
    print(f'{'-'*40}')
