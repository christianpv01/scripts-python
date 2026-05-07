def aumentar(n, p):
    return n + ( n * ( p / 100 ))

def diminuir(n, p):
    return n - ( n * ( p / 100 ))

def dobro(n):
    return n * 2

def metade(n):
    return n / 2

def resumo(n, a, d):
    print(f'{'-'*40}\n{'RESUMO DO VALOR':^40}\n{'-'*40}')
    print(f'{'Preço analisado':<16}:   R$ {n:.2f}')
    print(f'{'Dobro do preço':<16}:   R$ {dobro(n):.2f}')
    print(f'{'Metade do preço':<16}:   R$ {metade(n):.2f}')
    print(f'{f'{a}% de aumento':<16}:   R$ {aumentar(n, a):.2f}')
    print(f'{f'{d}% de aumento':<16}:   R$ {diminuir(n, d):.2f}')
    print(f'{'-'*40}')

    