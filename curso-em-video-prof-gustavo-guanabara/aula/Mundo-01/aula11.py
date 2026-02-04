#Cores
'''ANSI escape sequence
    \033['STYLE;TEXT;BACK'm
    STYLE -> 0 NONE / 1 BOLD / 4 UNDERLINE / 7 NEGATIVE
    TEXT  -> 30 BRANCO / 31 VERMELHO/ 32 VERDE / 33 AMARELO / 34 AZUL / 35 ROXO / 36 CIANO / 37 CINZA
    BACK  -> 40 BRANCO / 41 VERMELHO/ 42 VERDE / 43 AMARELO / 44 AZUL / 45 ROXO / 46 CIANO / 47 CINZA'''

print('\033[0;30;41mTeste\033[m')
print('')
print('\033[4;33;44mTeste\033[m')
print('')
print('\033[1;35;43mTeste\033[m')
print('')
print('\033[30;42mTeste\033[m')
print('')
print('\033[mTeste\033[m')
print('')
print('\033[7;30mTeste\033[m')
print('')
a = 3
b = 5
print('\033[43mOs valores são\033[m \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))