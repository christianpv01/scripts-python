def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip().replace(',','.')
        try:
            valor = float(n)
            return valor
        except ValueError:
            print('\033[0;31mERRO! "' + n + '" não é um valor monetário válido.\033[m')
