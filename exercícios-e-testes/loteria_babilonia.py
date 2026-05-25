# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.
# %%

from random import randint

sorteio = randint(1,15)

chutometro = 3

print(f'{'-'*40}\n{'LOTERIA BABILONIA':^40}\n{'-'*40}')

print(f'{'# Regras do jogo':^40}\n{'1. Você terá apenas 3 chances.':^40}\n{'2. Escolha um número entre 1 e 15.':^40}\n{'3. O bilhete é intransferível.':^40}\n')

for i in range(0,3):

    while True:
        
        try:
            
            chute = int(input(f'{f'{i+1}ª Tentativa: ':>26}'))
        
        except ValueError:
            
            print(f'\033[31m{'Digite um número interio entre 1 e 15.':^40}\033[m')
        
        else:

            if 0 < chute < 16:
                
                break

            else:

                print(f'\033[31m{'Digite um número interio entre 1 e 15.':^40}\033[m')

    if chute == sorteio:
    
        print(f'\033[32:m\n{'>> PARABÉNS!!':^40}\n{'>> VOCÊ VENCEU!!':^40}\033[m')
    
        break

    elif chute > sorteio and chutometro > 1:
    
        print(f'\033[33:m{'Tente um número menor.':^40}\033[m')
    
    elif chute < sorteio and chutometro > 1:
    
        print(f'\033[33:m{'Tente um número maior.':^40}\033[m')
    
    chutometro -= 1

else:
    print(f'\033[31m\n','Suas tentativas acabaram!! '.center(40),'\033[m')

print(f'\n{f'>>> O número sorteado foi {sorteio} <<<':^40}\n')

print(f'{'-'*40}\n{'Você jogou na Loteria Babilonia.':^40}\n{'Volte sempre!!':^40}\n{'-'*40}')