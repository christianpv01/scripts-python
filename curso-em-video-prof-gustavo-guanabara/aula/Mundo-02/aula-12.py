#condições aninhadas
'''
se       = if:   <- Executa o primeiro bloco
senão se = elif: <- Executa o segundo bloco / Não existe sem if do primeiro bloco / Mas pode existir sem else no final
senão    = else: <- Executa o terceiro bloco
    '''

nome = str(input('Qual é seu nome? '))
if nome == 'Christian':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))