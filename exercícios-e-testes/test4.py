# %%
def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    '''juros_compostos serve para calcular o retorno financeiro a partir de um aporte.
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para o cálculo do

    aporte:
        um número inteiro, que represente o valor em R$

    taxa:
        um número float entre 0 e 1 que represente o valor taxa de juros

    anos:
        um número inteiro >= 1 que representa o tempo que o investimento tera líquidez
    '''
    return aporte * (1 + taxa) ** anos

# %%

juros_compostos()

# %%
