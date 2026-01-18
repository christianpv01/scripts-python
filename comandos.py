
#Tipos Primitivos em Python
    #int - inteiro
    #float - real/ponto flutuante
    #bool - booleano/lógico
    #str - string/texto
#type() - mostra o tipo da variável
#No Python, podemos converter tipos de dados com as funções int(), float(), bool() e str()

#A função print() pode receber mais de um argumento, separados por vírgulas
#A função input() sempre retorna uma string

#Adição +
#Subtração -
#Multiplicação *
#Divisão /
#Divisão inteira //
#Resto da divisão %
#Potência **
#Ordem de precedência: 
    # 1º ( ) 
    # 2º ** 
    # 3º * / // % 
    # 4º + -

#Podemos usar a função round() para arredondar números
#Podemos usar a função abs() para obter o valor absoluto de um número
#Podemos usar a função pow() para calcular potências
#Podemos usar a função int() para converter um número para inteiro
#Podemos usar a função float() para converter um número para ponto flutuante

#{} - usado para definir dicionários
#[] - usado para definir listas
#() - usado para definir tuplas

#>  - maior que
#<  - menor que
#<> - diferente
#<= - menor ou igual
#>= - maior ou igual
#== - igual
#=  - atribuição
#and - e
#or  - ou
#not - não
#is  - é
#in  - em
#not in - não em

#.isspace() - verifica se todos os caracteres são espaços em branco
#.isalpha() - verifica se todos os caracteres são letras
#.isalnum() - verifica se todos os caracteres são alfanuméricos
#.isupper() - verifica se todos os caracteres estão em maiúsculas
#.islower() - verifica se todos os caracteres estão em minúsculas
#.istitle() - verifica se a string está em formato de título
#.isdecimal() - verifica se todos os caracteres são decimais
#.isdigit() - verifica se todos os caracteres são dígitos

#.count() - conta quantas vezes uma substring aparece na string
#.find() - encontra a posição da primeira ocorrência de uma substring na string
#.replace() - substitui uma substring por outra na string
#.strip() - remove espaços em branco do início e do fim da string
#.upper() - converte todos os caracteres da string para maiúsculas
#.lower() - converte todos os caracteres da string para minúsculas
#.title() - converte a string para formato de título
#.capitalize() - converte o primeiro caractere da string para maiúscula
#.split() - divide a string em uma lista de substrings
#.join() - junta uma lista de substrings em uma única string

#f-strings - formatação de strings usando f antes das aspas e {} para variáveis
#Exemplo: nome = "Maria"; idade = 30; print(f"{nome} tem {idade} anos")

#Método format() - formatação de strings usando {} e o método .format()
#Exemplo: nome = "Maria"; idade = 30; print("{} tem {} anos".format(nome, idade))

#Operadores de formatação em strings - %s (string), %d (inteiro), %f (ponto flutuante)
#Exemplo: nome = "Maria"; idade = 30; print("%s tem %d anos" % (nome, idade))