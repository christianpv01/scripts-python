'''Curso Python #15 - Interrompendo repetições while
    Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.
    Além disso, vamos aprender como trabalhar com as novas fstrings do Python.'''

#while True:  -- Loop infinito até ser False
    #break    -- Interrompe o loop

'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

'''n = cont = 0
while n != 999:
    n = int(input('Digite um númer: '))
    cont += 1'''

n = s = 0
while True:
    n = int(input('Digite um númer: '))
    if n == 999:
        break
    s += n
#print('A soma foi {}'.format(s))
print(f'A soma vale {s}')

nome = 'José'
idade = 33
salário = 987.35
print(f'O {nome:-^20} tem {idade} anos e ganha R${salário:.2f}.') # PYTHON 3.6+
print('O {} tem {} anos e ganha R${:.2f}.'.format(nome, idade, salário)) # PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2