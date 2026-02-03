#Cores
'''ANSI escape sequence
    \033['STYLE;TEXT;BACK'm
    STYLE -> 0 NONE / 1 BOLD / 4 UNDERLINE / 7 NEGATIVE
    TEXT  -> 30 BRANCO / 31 VERMELHO/ 32 VERDE / 33 AMARELO / 34 AZUL / 35 ROXO / 36 CIANO / 37 CINZA
    BACK  -> 40 BRANCO / 41 VERMELHO/ 42 VERDE / 43 AMARELO / 44 AZUL / 45 ROXO / 46 CIANO / 47 CINZA'''

nome = 'Christian'
print('Olá! Muito prazer em te conhecer, {}{}{}'.format('\033[4;34m',nome,'\033[m'))

cores = {'limpa':'\033[m', 
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'
         }
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'],nome,cores['limpa']))